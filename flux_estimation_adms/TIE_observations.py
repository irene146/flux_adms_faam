# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:59:33 2024

@author: FAAM_Student
"""

import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
from acruisepy import peakid
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from scipy.integrate import quad 
from scipy.stats import sem 


df = pd.read_csv(
    "MTGA_20220911b_merge_v3.csv", #datietime, lat, lon, height, conc
    header=[0], 
    parse_dates=True, 
    index_col=68,
    date_parser=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S%z")
)

df.index = df.index.tz_localize(None)


start_time = datetime.datetime(2022, 9, 11, 14, 20, 0)
end_time = datetime.datetime(2022, 9, 11, 15, 21, 31)
df = df.loc[start_time : end_time]

#peak ID 
ch4= df['CH4_ppm_pic']

#run peak ID (to be modified with newest version:https://github.com/wacl-york/acruise-peakid/tree/main/acruisepy)

#yellow line(plume threshold)x:limit to detect plume
#blue line (plume starting):where plume starts once it is detected

bg = peakid.identify_background(ch4, bg_sd_window=2, bg_sd_threshold=0.001, bg_mean_window=200)
#peakid.plot_background(ch4, bg, plume_sd_threshold=4, plume_sd_starting=0)

plumes = peakid.detect_plumes(ch4, bg, plume_sd_threshold=4, plume_sd_starting=0, plume_buffer=1)
#plumes['start']=plumes['start']-timedelta(seconds=4)
#plumes['end']=plumes['end']+timedelta(seconds=15)


peakid.plot_plumes(ch4, plumes)

ch4_areas = peakid.integrate_aup_trapz(ch4 - bg, plumes, dx=0.1)

heights= [43,37,102,105,169,236,236,302,296,364,360]
distance= [1,2,1,2,2,1,2,1,2,1,2]

speed=[]
# calculate the average speed for each plume interval
for i, row in plumes.iterrows():
    start_time = row['start']
    end_time = row['end']
    mask = (df.index >= start_time) & (df.index <= end_time)
    avg_speed = df.loc[mask, 'IRS_GS'].mean()
    speed.append(avg_speed)

speed =np.array(speed)

#convert peak area from ppmm to ppbs 

area_ppbs = np.array(ch4_areas['area']*speed*1000)

peak_areas = pd.DataFrame({'height_m': heights, 'distance': distance, 'area_ppbs': area_ppbs})


peak_areas_close = peak_areas[peak_areas['distance'] <=1.5]
peak_areas_far = peak_areas[peak_areas['distance'] >=1.5]
heights_far =np.array(peak_areas_far['height_m'], dtype=int)
pk_far =np.array(peak_areas_far['area_ppbs'], dtype=int)

#GAUSSIAN APPROACH
'''
def gaussian(x, a, b, c):
    return a * np.exp(-(x - b)**2 / (2 * c**2))

p0=(2370.426, 309.4721, 96.39894)

fit,err = curve_fit(gaussian, heights_far, pk_far, p0=p0)

a1,b1,c1 =fit
    
perr = np.sqrt(np.diag(err))

def integrand(x,a1,b1,c1):
    return gaussian(x,a1,b1,c1)

# Define the Monte Carlo simulation function to propagate parameter uncertainties
def monte_carlo_integration(func, params, param_errors, x_min, x_max, num_samples=5000):
    integral_values = []
    for _ in range(num_samples):
        sampled_params = np.random.normal(params, param_errors)
        integral_value, _ = quad(func, x_min, x_max, args=tuple(sampled_params))
        integral_values.append(integral_value)
    return np.mean(integral_values), np.std(integral_values)

# Assuming fit_params contains the best-fit parameters and fit_errors contains the errors
fit_params = fit
fit_errors = perr

# Integration limits
x_min = 35
x_max = 360

# Perform Monte Carlo integration
integral_value, integral_error = monte_carlo_integration(integrand, fit, perr, x_min, x_max)
'''

#trapezoidal approach 
dx=1
area_tap=np.trapz(pk_far, x=heights_far,dx=dx)
x = np.linspace(35, 360, 10000)
plt.figure(figsize=(10, 6))
plt.scatter(heights_far, pk_far, label='Peak areas ppb.s', color='blue')
plt.plot(heights_far, pk_far)

plt.xlabel('Height')
plt.ylabel('Peak Area')


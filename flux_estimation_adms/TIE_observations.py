# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:59:33 2024

@author: FAAM_Student

IE and TIE caclulations for observational (aircraft)
Steps: 
1. Read data (csv)
2. Calculate IE with peak ID 
3. Convert IE into the correct units 
4. Calculate TIE with Gaussian or trapezoidal approach 
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
    "MTGA_20220911b_merge_v3.csv", #datietime, lat, lon, height, conc, speed
    header=[0], 
    parse_dates=True, 
    index_col=68, #establish colum number of your datetim
    date_parser=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S%z")
)
df.index = df.index.tz_localize(None)

"""
 MTGA_20220911b_merge_v3.csv": Filename of the CSV file. Change this to your actual filename.
    - header=0: Indicates that the first row of the file is the header.
    - parse_dates=True: Ensures that date columns are parsed as datetime objects.
    - index_col=68: The 0-based index of the column containing datetime information. Change this to match your datetime column.
    - date_parser=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S%z")
    Lambda function to parse the datetime format in the CSV. Adjust the format string to match your specific datetime format.
"""


start_time = datetime.datetime(2022, 9, 11, 14, 20, 0)
end_time = datetime.datetime(2022, 9, 11, 15, 21, 31)
df = df.loc[start_time : end_time]
"""
Filter your dataframe by the start and end time of your sampling period (established in the plot_ch4 script)
"""

#################################
#IE calculations
#################################

# Select the column in your DataFrame with the gas concentration data
ch4 = df['CH4_ppm_pic']


# Run peak identification. Refer to the user guide: https://github.com/wacl-york/acruise-peakid/tree/main/acruisepy

# Identify background levels of CH4 concentration
bg = peakid.identify_background(ch4, bg_sd_window=2, bg_sd_threshold=0.001, bg_mean_window=200)

# Plot the identified background
peakid.plot_background(ch4, bg, plume_sd_threshold=4, plume_sd_starting=0)

# Detect plumes based on the background levels
plumes = peakid.detect_plumes(ch4, bg, plume_sd_threshold=4, plume_sd_starting=0, plume_buffer=1)

# Adjust the start and end times of the detected plumes to account for potential underestimation
plumes['start']=plumes['start']-timedelta(seconds=4)
plumes['end']=plumes['end']+timedelta(seconds=15)


# Plot the detected plumes
peakid.plot_plumes(ch4, plumes)

# Integrate the area under the curve for each plume to obtain IE values in ppm*seconds
ch4_areas = peakid.integrate_aup_trapz(ch4 - bg, plumes, dx=0.1)
"""
Peak ID integration function uses the trapezoidal approach.
Change dx depending on the measurement rate of the instrument: 1 for 1Hz, 0.1 for 10Hz.
"""


heights =[]
# calculate the average height for each plume 
for i, row in plumes.iterrows():
    start_time = row['start']
    end_time = row['end']
    mask = (df.index >= start_time) & (df.index <= end_time)
    avg_speed = df.loc[mask, 'GPS_ALT'].mean() #change GPS_ALT for the column name of the height measurements in your df
    speed.append(avg_speed)

heights =np.array(heights)

# Example distances list for this specific case
distance= [1,2,1,2,2,1,2,1,2,1,2] 


speed=[]
# calculate the average speed for each plume interval
for i, row in plumes.iterrows():
    start_time = row['start']
    end_time = row['end']
    mask = (df.index >= start_time) & (df.index <= end_time)
    avg_speed = df.loc[mask, 'IRS_GS'].mean() #change IRS_GS for the column name of the GROUND SPEED measurements in your df
    speed.append(avg_speed)

speed =np.array(speed)

# Convert IE values from ppm*seconds to ppb*meters (verify units of your DataFrame)
area_ppbs = np.array(ch4_areas['area']*speed*1000)

#Put everything into a df for easy visualisation 
peak_areas = pd.DataFrame({'height_m': heights, 'distance': distance, 'area_ppbs': area_ppbs}) 

# Filter by distances for this specific case
peak_areas_close = peak_areas[peak_areas['distance'] <=1.5]
peak_areas_far = peak_areas[peak_areas['distance'] >=1.5]
heights_far =np.array(peak_areas_far['height_m'], dtype=int)
pk_far =np.array(peak_areas_far['area_ppbs'], dtype=int)


#################################
#TIE calculations 
#################################
"""
Two approaches you can calculate TIE 
Gaussian approach : fit a Gaussian (or half Gaussian) to your dataset with curve fit function
    Guess parameters (p0) are not the best, sometimes used Matlab to get a fit
    Monte Carlo integration to get errors
Trapezoidal approach: 
A lot shorter and less fiddely. 
"""
#GAUSSIAN APPROACH

def gaussian(x, a, b, c):
        """Gaussian function for curve fitting."""
    return a * np.exp(-(x - b)**2 / (2 * c**2)) 

#inital guess parameters for the fit
p0=(2370.426, 309.4721, 96.39894) 

fit,err = curve_fit(gaussian, heights_far, pk_far, p0=p0) 
"""
curve fit arguments: 
(funciton, x-axix, y-axix, guess parameters)  change the x and y axis  

fit: Optimal values for the parameters
err: The estimated approximate covariance of fit.
"""
a1,b1,c1 =fit  
    
perr = np.sqrt(np.diag(err)) #one standard deviation errors on the parameters

def integrand(x,a1,b1,c1):
    return gaussian(x,a1,b1,c1)
"""
defines integrand of the gaussian 
"""

# Define the Monte Carlo simulation function to propagate parameter uncertainties
def monte_carlo_integration(func, params, param_errors, x_min, x_max, num_samples=5000): 
     """
    Perform Monte Carlo integration to propagate parameter uncertainties.
    
    Args:
        func (callable): The integrand function.
        params (list): Best-fit parameters for the integrand.
        param_errors (list): Errors associated with the parameters.
        x_min (float): Minimum x value for integration.
        x_max (float): Maximum x value for integration.
        num_samples (int): Number of samples for the Monte Carlo simulation.
    
    Returns:
       Mean and standard deviation of the integral values.
    """
    integral_values = []
    for _ in range(num_samples):
        sampled_params = np.random.normal(params, param_errors)
        integral_value, _ = quad(func, x_min, x_max, args=tuple(sampled_params))
        integral_values.append(integral_value)
    return np.mean(integral_values), np.std(integral_values)

fit_params = fit
fit_errors = perr

# Integration limits. Change depending on your domain (min and max heights) 
x_min = 35
x_max = 360

# Perform Monte Carlo integration
integral_value, integral_error = monte_carlo_integration(integrand, fit, perr, x_min, x_max)
"""
Output: integral_value: TIE in ppb*meters^2
"""

#TRAPEZOIDAL APPROACH 
dx=1 #define dx as 1 (meters) 
area_tap=np.trapz(pk_far, x=heights_far,dx=dx)
"""
function arguments: 
(y-axis, x=x-axis, dx=dx) 
"""

#plot
x = np.linspace(35, 360, 10000)
plt.figure(figsize=(10, 6))
plt.scatter(heights_far, pk_far, label='Peak areas ppb.s', color='blue')
plt.plot(heights_far, pk_far)

plt.xlabel('Height')
plt.ylabel('Peak Area')


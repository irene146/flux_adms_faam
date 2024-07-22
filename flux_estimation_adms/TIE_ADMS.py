# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:58:03 2024

@author: FAAM_Student
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import numpy as np
import glob
from scipy.optimize import curve_fit
from scipy.integrate import quad
import os 

#import faam data converted to  xy coord
df_fgga2= pd.read_csv("faam_x_y.csv", header=0, index_col=0)


#degine gaussian function 
def gaussian(x, a, b, c):
    return a *np.exp(-((x-b)**2)/(2*c**2))

#define adms_peak area function
def ADMS_peak_area(z_colum, df):
    #grab only lats and lons  for one of the transects , you assume that transects are supersimposed 
    df_fgga = df_fgga2.loc[(df_fgga2['HGT_RADR'] > 280) & (df_fgga2['HGT_RADR'] <= 350)]
    #interpolate adms methane data so that it matches faam coordinates. gives ch4 adms enhancements just for faam coordiantes(DAVE)
    adms_interpolated2 = griddata((df['X(m)'], df['Y(m)']), df[z_colum], (df_fgga.X, df_fgga.Y))
    adms_interpolated = np.nan_to_num(adms_interpolated2, nan=0)
    #calculate the distance of the faam transect with pythagoras(dave)
    x = df_fgga.X
    y = df_fgga.Y
    dist_series= (((x - x.shift())**2 + (y - y.shift())**2)**0.5).cumsum().fillna(0)
    #turn dist into an array
    dist = np.array(dist_series, dtype=float)
    #calculate max methane conc
    max_index = np.argmax(adms_interpolated)

    #find corresponding distance to max ch4 value for better fit 
    distance_at_max_ch4 = dist[max_index]
    #parameters correspond to width, mean, and sd of the initial gaussian fit ans are guesses
    p0=[6000, distance_at_max_ch4,1000]
    fit, cov = curve_fit(gaussian, dist, adms_interpolated, p0=p0)

    a, b, c = fit
    #establish limits on the x axis for the integral
    min_limit_dist = np.min(dist)
    max_limit_dist = np.max(dist)
    
    #define integral function for gaussian function 
    def integrand(x):
        return gaussian(x, a, b, c)
    #integreate gaussian function 
    int_gauss_result, int_error = quad(integrand, min_limit_dist, max_limit_dist)
    #ADMS_peak_area returns the peak area for a single peak ant a single height and the error 
    return int_gauss_result, int_error
    
#directory with all yor gst files 
directory = "D://wellehadA_volume//wellheadA//sstemp//t10//550//"
#gst file that you want to analyse 
gst_file = "wellheada_cerc_corrections_temp_ss10.levels.gst"

    

df = pd.read_csv(gst_file, header=0)
# delete useless columns
df.drop(columns=['Year', 'Day', 'Hour', 'Time(s)', 'Z(m)'], inplace=True)

heights = []
peak_areas = []
peak_errors = []
   
for i, z_column in enumerate(df.columns[2:]): # [2:] because x and y are the two first columns 
    #calculate peak area (gaussian) and error for each height adnd add them to the list 
        peak_area, peak_error = ADMS_peak_area(z_column, df)
        peak_areas.append(peak_area)
        
        peak_errors.append(peak_error)
        # extract the Z value from the column name
        height = z_column.split('=')[1].split('m')[0]
        heights.append(height)
        
        
# =============================================================================
# code up to here takes a long time to run as gst files are big, can save into a csv and do curve fit latetr 
# =============================================================================

      
#after loop you have 3 lists, with heights, peak areas and peak errors for a single folder(flux) (similar to peak ID data)
height_area_results = {'heights': heights, 'peak_area': peak_areas, 'peak_area_error': peak_errors}

# convert the dictionary to a dataframe 
height_area_results = pd.DataFrame(height_area_results)
height_area_results.to_csv('cerc_temp_sstemp10.csv')



#TIE calculation
'''
df_1 =pd.read_csv('550cerc_temp_sstemp.csv', index_col=0, header=0)
x_data_adms_1 = np.array(df_1['heights'])
y_data_adms_1 = np.array(df_1['peak_area'])




#Gaussian approach 

def half_gaussian(x,a1,b1,c1):
   return a1*np.exp(-((x-b1)/c1)**2)

guess =(25658, 69.2191,479.5105)

fit_1,err_1 = curve_fit(half_gaussian, x_data_adms_1, y_data_adms_1, p0=guess)

a1_1,b1_1,c1_1 =fit_1
    
perradms_1 = np.sqrt(np.diag(err_1))


def integrand(x,a1,b1,c1):
    return half_gaussian(x,a1,b1,c1)

# Define the Monte Carlo simulation function to propagate parameter uncertainties
def monte_carlo_integration(func, params, param_errors, x_min, x_max, num_samples=5000):
    integral_values = []
    for _ in range(num_samples):
        sampled_params = np.random.normal(params, param_errors)
        integral_value, _ = quad(func, x_min, x_max, args=tuple(sampled_params))
        integral_values.append(integral_value)
    return np.mean(integral_values), np.std(integral_values)


# Integration limits
x_min = 75
x_max = 595

# Perform Monte Carlo integration
integral_value_adms_1, integral_error_adms_1 = monte_carlo_integration(integrand, fit_1, perradms_1, x_min, x_max)


x = np.linspace(75, 600, 10000)

plt.figure(figsize=(10, 6))
plt.scatter(x_data_adms_1, y_data_adms_1, label='ADMS', color='green')
plt.plot(x_data_adms_1, half_gaussian(x_data_adms_1, *fit_1), label='Gaussian fit to ADMS', color='green')
upper_bound = half_gaussian(x_data_adms_1, *(fit_1 + perradms_1))
lower_bound = half_gaussian(x_data_adms_1, *(fit_1 - perradms_1))
#plt.fill_between(x_data_adms_1, upper_bound, lower_bound, color='lightgreen', alpha=0.4, label='Fit Uncertainty ADMS 2D uniform wind')
plt.fill_between(x_data_adms_1, upper_bound, lower_bound, color='lightblue', alpha=0.4, label='Fit Uncertainty ADMS MBL')

plt.xlabel('Height (m)', fontsize = 14)
plt.ylabel('Peak Area (ppb*m)',fontsize = 14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.legend()
plt.show()
#plt.savefig('peak_areas_faam_adms_pbl_mbl.png', dpi = 2000)

#trapezoidal approach: 
    
dx=1
area_tap=np.trapz(df_1, x=x_data_adms_1,dx=dx)

''' 
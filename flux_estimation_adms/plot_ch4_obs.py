# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:39:02 2024

@author: FAAM_Student

Use this script to identify how the flight was conducted,  your sampling lat lons and heights as well as the start and end time of your sampling period. 
Identify the height and position order of the flight passes (eg. top to bottom or vivice-versa, intercalated, etc)  

"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('MTGA_20220911b_merge_v3.csv', header =0, index_col= 0) 
  """
  MTGA_20220911b_merge_v3.csv is a sample from DLR, canhge it to your csv 
  This df should at least include lat, lon, heihgt, datetime column and conc of desired gas 
  """
df =df[df['CH4_ppm_pic'] >=1.87] #to remove background and adjust colorscale 
df=df[df['GPS_ALT'] <=600]
df = df.loc[(df['GPS_LON'] >= 10.65) & (df['GPS_LON'] <= 10.8)]
df = df.loc[(df['GPS_LAT'] >= -6) & (df['GPS_LAT'] <= -6.5)]
  """
  Run the script first with lines 21-23 commented to see full flight
  Adjust lat lon height parameters on the interactive 3D plot to see where is your sampling area
  Tweak lines 21-23 until you narrow down your sampling area
  Note down start and end times of the df after you have narrowed down the smapling area
  """

#plot
latitudes = df['GPS_LAT'].values
longitudes = df['GPS_LON'].values
heights = df['GPS_ALT'].values
concentrations = df['CH4_ppm_pic'].values

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the concentration values as a color-coded line
scatter = ax.scatter(latitudes, longitudes, heights, c=concentrations, cmap='viridis')

# Add color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Concentration')

# Set labels for each axis
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Height')

# Show the plot
plt.show()

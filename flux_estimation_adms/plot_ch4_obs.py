# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:39:02 2024

@author: FAAM_Student
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('MTGA_20220911b_merge_v3.csv', header =0, index_col= 0)
df =df[df['CH4_ppm_pic'] >=1.87]
df=df[df['GPS_ALT'] <=600]
df = df.loc[(df['GPS_LON'] >= 10.65) & (df['GPS_LON'] <= 10.8)]
#df = df.loc[(df['GPS_LAT'] >= -6) & (df['GPS_LAT'] <= -6.5)]


#df_ch4 = df[['CH4_ppm_pic', 'GPS_ALT', 'GPS_LAT', 'GPS_LON]']]

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
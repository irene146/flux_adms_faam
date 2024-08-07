# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:39:02 2024

Author: FAAM_Student

This script is used to analyze flight data, identify the sampling latitudes, longitudes, and heights,
as well as determine the start and end times of the sampling period. It also helps to identify the 
height and position order of the flight passes (e.g., top to bottom, vice versa, intercalated, etc.).

Steps:
1. Load the flight data from a CSV file.
2. Filter the data based on methane concentration, altitude, and geographical bounds.
3. Plot the filtered data in a 3D plot to visualise the sampling area.

Instructions:
1. Adjust the CSV filename to match your data file.
2. Ensure the data file includes columns for latitude, longitude, height, datetime, and gas concentration.
3. Initially run the script with lines 21-23 commented out to see the full flight path.
4. Adjust latitude, longitude, and height parameters to narrow down your sampling area.
5. Note the start and end times of the filtered data after narrowing down the sampling area.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the flight data from a CSV file
df = pd.read_csv('MTGA_20220911b_merge_v3.csv', header=0, index_col=0) 
"""
MTGA_20220911b_merge_v3.csv is a sample file from DLR; change it to your CSV filename.
Ensure the dataframe includes columnscolumns for latitude, longitude, height, datetime, and gas concentration.
"""
df =df[df['CH4_ppm_pic'] >=1.87] #to remove background and adjust colorscale 
df=df[df['GPS_ALT'] <=600]
df = df.loc[(df['GPS_LON'] >= 10.65) & (df['GPS_LON'] <= 10.8)]
df = df.loc[(df['GPS_LAT'] >= -6) & (df['GPS_LAT'] <= -6.5)]
  """
Run the script first with the lines above commented out to see the full flight path.
Adjust latitude, longitude, and height parameters on the interactive 3D plot to identify your sampling area.
Tweak the lines above until you narrow down your sampling area.
Note down the start and end times of the filtered dataframe after narrowing down the sampling area.
  """

#Interactive 3d plot
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

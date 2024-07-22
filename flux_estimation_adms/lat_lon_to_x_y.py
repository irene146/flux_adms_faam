# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:40:10 2024

@author: FAAM_Student
"""
import math
import pandas as pd
import datetime 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

df =pd.read_csv('fgga_core_b689.csv', header=[0], parse_dates=True, index_col=0,)

start_time = datetime.datetime(2012, 4, 3, 13, 45, 0)
end_time = datetime.datetime(2012, 4, 3, 14, 40, 0)
df = df.loc[start_time : end_time]


df = df.loc[(df['LON_GIN'] >= 1.5) & (df['LON_GIN'] <= 2)]
df = df.loc[(df['LAT_GIN'] >= 56.90) & (df['LAT_GIN'] <= 57)]

df = df.iloc[:, :3]

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Radius of the Earth in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi/2) * math.sin(delta_phi/2) + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda/2) * math.sin(delta_lambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    
    return d

def latlon_to_xy(lat, lon, ref_lat, ref_lon):
    # Reference point
    ref_x = haversine(ref_lat, ref_lon, ref_lat, lon)
    ref_y = haversine(ref_lat, ref_lon, lat, ref_lon)
    
    # Target point
    x = haversine(ref_lat, ref_lon, ref_lat, lon)
    y = haversine(ref_lat, ref_lon, lat, ref_lon)
    
    return x, y

# Reference point
#PUQ
# =============================================================================
# ref_lat = 57.011046
# ref_lon = 1.836386
# =============================================================================

#wellhead a 
ref_lat = 57.011619
ref_lon = 1.838534

#convert rows of df from lat lon to x y 
df['X'], df['Y'] = zip(*df.apply(lambda row: latlon_to_xy(row['LAT_GIN'], row['LON_GIN'], ref_lat, ref_lon), axis=1))

#convert df to csv
# Calculate max and min values for X and Y
max_x = df['X'].max()
min_x = df['X'].min()
max_y = df['Y'].max()
min_y = df['Y'].min()

# Create a dictionary for the results
maxmin_dict = {
    'X': {'max': max_x, 'min': min_x},
    'Y': {'max': max_y, 'min': min_y}
}

# Create a DataFrame from the dictionary
max_min_df = pd.DataFrame(maxmin_dict)

df.reset_index(drop=True, inplace=True)
df = df.iloc[:, 2:]

#plot
plt.scatter(df['X'], df['Y'], color='blue', marker='o', label='Data Points')

# Plot max and min points
plt.scatter([max_x, min_x], [max_y, min_y], color='red', marker='x', label='Max/Min Points')

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Equivalent of x and y values for sampled alt lons')

# Add legend
plt.legend()

# Show plot
plt.show()
'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

latitudes = df['X'].values
longitudes = df['Y'].values
heights = df['HGT_RADR'].values

# Plot the concentration values as a color-coded line
scatter = ax.scatter(latitudes, longitudes, heights, )


# Set labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Height')

# Show the plot
plt.show()
'''
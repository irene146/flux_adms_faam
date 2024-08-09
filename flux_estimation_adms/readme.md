# Flux estimation

All the scripts there should run with their corresponding sample data file as an example. 

### Step 1: Plot CH4

The `plot_ch4` script can be used with any gas. It is used with your observational data. Identify the sampling lat/long and height limits, as well as the start and end times of your sampling period. This script also helps determine the order of flight passes (e.g., top to bottom or vice versa). Your dataset needs to have a datetime column, height, lat, lon and concenrtation of desired gas. 

### Step 2: TIE Observations

Run `TIE_observations` to calculate the TIE Total integrated enhancement for the observations. Your dataset needs to include the following variables:
- `datetime`
- `lat`
- `lon`
- `height`
- `concentration` of the desired gas
- `ground speed` of the aircraft

### Step 3: Convert Coordinates

Use the `lat_lon_to_x_y` script: The ADMS model gives a 3D grid where the coordinates are in an unspecified Cartesian system. This means your emission source is located at the point (0,0) in metres, and the rest of the grid is in X, Y, and Z coordinates, also in metres, relative to this source.
To match aircraft observations with this model grid, you need to convert the latitude, longitude, and altitude data from the aircraft into X, Y, and Z coordinates in metres, based on the position of the emission source.

### Step 4: Run



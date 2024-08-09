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

### Step 4 create model imput .met file: 
Run `create_file_adms`: 
The MET file must be organised with the following structure (the code does it for you):

 VARIABLES:

Specify the number of variables in the file. 
 Variable Names:

List the names of the variables you want to include:
- **YEAR** – The year of the data.
- **TDAY** – The Julian day of the year.
- **THOUR** – The hour of the day (24-hour format).
- **T0C** – Temperature in degrees Celsius.
- **U** – Wind speed in meters per second (m/s).
- **PHI** – Wind direction in degrees.
- **SIGMATHETA** – Standard deviation of wind speed (to account for variability in wind speed).
- **CL** – Cloud cover in oktas (0-8 scale).
- **H** – Boundary layer height in meters.
- **PRECIP** – Precipitation.

Input data should be in the same order as the variables listed above. Each data point should be separated by commas.

 Data Collection 

Temporal Resolution:

The highest resolution of meteorology data allowed in ADMS is 1h, and for the input settings used, ADMS outputs a different modelled scenario for each hour of met data provided (1 line of data = 1h). To avoid this, the meteorology variables obtained while the aircraft was flying over the source are averaged to 1h of met data as long as they are consistent, outputting a single dispersion. This is to avoid multiple model outputs and allow easier analysis.

 Variable Considerations:

- For variable names and units, check the ADMS 6 user manual on page 342.
- The main idea with input met data is to include as much as possible from the aircraft data, but if you don’t know a value, it is better to let the model calculate rather than guessing yourself. 

 Temperature (T0C):

ADMS assumes temperature measurements are taken 2 metres above the ground. If possible, use radiosonde data for more accurate temperature values.

 Wind Speed and Direction (U and PHI):

Ensure these are consistent during the sampling period. If variability in wind speed is observed, include the standard deviation as the **SIGMATHETA** variable.

 Cloud Cover (CL):

Measured in oktas. This can be determined from camera footage taken during the sampling period and provided by a meteorologist.

 Boundary Layer Height (H):

Critical for dispersion modelling, ensure accurate measurements are used.

 Precipitation (PRECIP):

Add sea surface temperature if the marine boundary layer option is used in ADMS and it is not assumed to be neutral.


 

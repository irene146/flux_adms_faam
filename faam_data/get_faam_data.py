"""
Created on Thu Apr 11 11:03:46 2024

@author: Irene Monreal and Dave Sproson <3

Lines you need to modify: 27,29,31,40,49,62,70,73,82,84-89
"""
import nappy
import netCDF4
import sys
import pandas as pd
import numpy as np
from faamda.wrapper import FAAM
from collections import OrderedDict


#import nappy in a wierd way from: https://github.com/cedadev/nappy, ask dave 
#import FAAM library from https://github.com/FAAM-146/faam-datautils

# =============================================================================
#Obtaining FAAM data from the core file
#=============================================================================


#first, download flight core file from CEDA https://data.ceda.ac.uk/badc/faam

faam = FAAM(['d:\\your_directory']) #recognises faam core files on that directory 
faam.flights #recognises what flights you have available 
CXXX = faam['flightnumber'].core #write fligh tnumebr you want to get data from 

data = CXXX[['LAT_GIN', 'LON_GIN', 'HGT_RADR']] #select variables that you need 

#a full guide on variables available, how are they measured and what units they are in:
    #https://www.faam.ac.uk/sphinx/coredata/dynamic_content/coredata.html#variables
    
data = data.interpolate().dropna() #interpolte over all values of lat long gin so that frequencies match 

#for unit conversions: https://github.com/FAAM-146/decades-ppandas/blob/master/ppodd/utils/conversions.py

data.to_csv('core_data_flightnumber')


# =============================================================================
# Joining FGGA data and FAAM data in the same dataset
# =============================================================================

#fgga data is a .na file available in the ceda archive

ifile = "directory of .na file + filename.na"    
ds = nappy.openNAFile(ifile)  #open na file with nappy
ds.readData() #read data 


#fix timestamp 
time_units = ds.getIndependentVariable(0)[1] #recognises time data on file
time_units = time_units.replace('fractional', '').replace('elapsed','').strip() #remove wierd names 
timestamp = netCDF4.num2date(ds.X, time_units) #converts number to time format  

#turn the .na file into a df 
_dict = OrderedDict()  #create empty organised dictionary (remebers what was added first )
_dict['timestamp'] = timestamp #adds timestamp to the dictionary 
for i, v in enumerate(['co2_ppm', 'co2_flag', 'ch4_ppb', 'ch4_flag']): #interates over the strings gettig both index (i) and value (v)      
                                                                       #CHANGE column names depending on the gases that you are interested in 
    #print(f'reading {v}')
    _dict[v] = ds.V[i] 
df = pd.DataFrame(_dict) #converts _dic to a pandas dataframe
df = df.set_index('timestamp') #set index to timestamp column 


df.to_csv('fgga_flightnumber.csv') 

#can avoid this step if you don't want to save fgga data on its own
fgga = pd.read_csv('fgga_flightnumber.csv', index_col=[0], parse_dates=True, date_format="ISO8601")  #import fgga data correcting for date format 

new_index = data.index.union(fgga.index).sort_values()  #join indexes for both fgga and core data (they dont match)
data2 = data.reindex(new_index).interpolate().loc[fgga.index] #create new df where you interpolate lat lon hgt values over fgga values as well
                                                              #then after .loc[fgga.index] only picks values that had fgga time           
for i in fgga.columns: #paste fgga columns to data 2 so that timestamp is the same 
    data2[i] = fgga[i]
    

data2.to_csv('fgga_core_flightnumber.csv')

#reading data for a single gas 

ch4_CXXX = data2.drop(columns=['co2_ppm', 'co2_flag',])

ch4_CXXX.loc[df.co2_flag>0] = np.nan #locate what values of co2 have a flag and convert them to nans(flag =1 means fgga was calibrating)
ch4_CXXX.to_csv('ch4_CXXX.csv')

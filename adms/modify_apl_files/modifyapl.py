
#if you only have 1 file to modify
# =============================================================================
# import os 
# from modelconfig import ModelConfig
# mc = ModelConfig()
# import glob 
# 
# mc.read('yourfile.ini') #you need to save your.apl file as an .ini file 
# 
# create lsit with desired intervals 
# min_value = 0
# max_value = 10 
# interval =  2
# 
# data = list(range(min_value, max_value +1, interval))
# 
# function that reads initial.ini file modifies value. 
# modify code as[header][variable]
# for x  in data : 
#     mc['ADMS_SOURCE_DETAILS']['SrcPolEmissionRate'] = str(x)+'e+0'
#     mc.write('CXX_variable_' + str(x) +'.apl')
# 
# 
# directory = "D://adms6.old//modify _apl_files"
# 
# 
# ini_files = glob.glob(directory + "*.ini")
# =============================================================================



#if you want to modify more than 1 apl file at the same time
# =============================================================================
#create list with desired values 
# min_value = 550
# max_value = 1260 
# interval =  100
# data = list(range(min_value, max_value +1, interval))
# 
# 
# from modelconfig import ModelConfig
# import glob
# import numpy as np
# 
# for f in glob.glob('*.ini'):
#     mc = ModelConfig()  
#     mc.read(f)
#     
#     for x  in data : 
#         mc['ADMS_SOURCE_DETAILS']['SrcPolEmissionRate'] = str(x)+'e+0'
#         mc.write(f'{f.split(".")[0]}_{x}.apl')
# 
# =============================================================================

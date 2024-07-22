# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:47:49 2024

@author: Irene Monreal and original version in R: Beth Nelson
"""

# =============================================================================
#Create .MET file for ADMS 
# =============================================================================

#store all your met values values as: 
    # YEAR = 2024
    # THOUR = 12 etc. 
# for a description of ADMS met imput values see user manual
# for met values available from faam, see https://www.faam.ac.uk/sphinx/coredata/dynamic_content/coredata.html#variables


#store all the met values with the corresponding ADMS  variable names
met_data = {
    'YEAR': [YEAR],
    'TDAY': [TDAY],
    'THOUR': [THOUR],
    'T0C': [mean_temp],
    'U': [ws_avg],
    'PHI': [wdir_avg],
    'SIGMATHETA': [wdir_sd],
    'CL': [CL],
    'H': [blh],
    'PRECIP': [PRECIP]
}

met_data = pd.DataFrame(met_data)


# function to create met data file for ADMS input
def print_adms_met(data, path):
    # get column names
    names = data.columns
    
    # gind length of names
    len_names = len(names)
    
    # collapse names into one string, separated by \n (new line)
    names_str = "\n".join(names)
    
    # create header in the same way
    header = f"VARIABLES:\n{len_names}\n{names_str}\nDATA:\n"
    
    # write header
    with open(path, 'w') as f:
        f.write(header)
    
    # Write the rest of the table (without col/row names)
    data.to_csv(path, mode='a', sep=',', header=False, index=False)

#save .met file 

print_adms_met(met_data, 'yourdirectory/fligtnumber_met.met')
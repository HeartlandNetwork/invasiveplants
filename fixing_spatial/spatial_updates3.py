

###############################################################
#
#   spatial_updates3.py
#   importing new thru 2023 
#   and fixing spatial coordinates
#   in invasive_plants data package
#
#   Gareth Rowell - 20240925
#
###############################################################

# start the IPython session here:
# C:\Users\GRowell\invasive_plants

import pandas as pd
import matplotlib.pyplot as plt


# set option to display all data
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# load spatial center points 

df_arpo = pd.read_csv("ArpoInpCenterPts.csv")
df_cuva = pd.read_csv("CuvaInpCenterPts.csv")
df_efmo = pd.read_csv("EfmoInpCenterPts.csv")
df_gwca = pd.read_csv("GwcaInpCenterPts.csv")
df_heho = pd.read_csv("HehoInpCenterPts.csv")
df_hocu = pd.read_csv("HocuInpCenterPts.csv")
df_home = pd.read_csv("HomeInpCenterPts.csv")
df_hosp = pd.read_csv("HospInpCenterPts.csv")
df_libo = pd.read_csv("LiboInpCenterPts.csv")
df_peri = pd.read_csv("PeriInpCenterPts.csv")
df_pipe = pd.read_csv("PipeInpCenterPts.csv")
df_tapr = pd.read_csv("TaprInpCenterPts.csv")
df_wicr = pd.read_csv("WicrInpCenterPts.csv")


# concatenate all 

df_all = pd.concat([df_arpo, df_cuva, df_efmo, df_gwca], ignore_index=True)
df_all = pd.concat([df_all, df_heho, df_hocu, df_home, df_hosp], ignore_index=True)
df_all = pd.concat([df_all, df_libo, df_peri, df_pipe, df_tapr, df_wicr], ignore_index=True)

df_all.to_csv("df_all.csv", sep=',', encoding='utf-8')

















LatitudeInDecimalDegrees

df["LatitudeInDecimalDegrees"].plot.hist

# 
# select columns

df_pub = df_pub[['ParkName','ParkCode','LocationID','PeriodID', \
    'CoverClassInMetersSquared','CommonName','ScientificName', \
    'Date','Type','BasisofRecord','TaxonRank']]  
df_hosp = df_hosp[['InpID','Acres','LocationID','Lon_DD', 'Lat_DD']]
df_home = df_home[['InpID','Acres','LocationID','Lon_DD', 'Lat_DD']]

# df_hosp LocationID is incomplete
# LocationID is an integer

df_hosp[['LocationID']] = df_hosp[['LocationID']].astype(str)
df_hosp[['LocationID']] = 'HOSP_InvPla_' + df_hosp[['LocationID']]

  # display columns

print("pub ---------------------------------")
print(df_pub.head(3))
print("hosp ---------------------------------")
print(df_hosp.head(3))
print("home ---------------------------------")
print(df_home.head(3))
print("---------------------------------")


# this script is fixing hosp and home
# complete this and test in Power BI
# if its good, reload published csv and filter out old
# home and hosp and insert new home and hosp

# left join df_pub on df_hosp and df_  

result = df1.merge(df2, on='team', how='left')



    



# Select the 'Name' and 'City' columns
selected_columns = df[['Name', 'City']]

print(selected_columns)



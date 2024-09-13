

###############################################################
#
#   view_home_hosp_coord.py
#   correcting lat/long dd for HOME and HOCU
#   in invasive_plants data package
#   this script is to view the distributions of
#   decimal degree latitudes and longitudes
#   for HOME and HOSP - to be used before and
#   after corrections are made
#
#   Gareth Rowell - 20240913
#
###############################################################

# start the IPython session here:
# C:\Users\GRowell\invasive_plants


import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df_inv = pd.read_csv("HTLN_InvasivePlants_Monitoring.csv")

#LatitudeInDecimalDegrees

df_inv["LatitudeInDecimalDegrees"].plot.hist()
plt.xlabel("Latitude")
plt.ylabel("Frequency")
plt.title("Error Detection")
plt.show()

# need to filter for hosp and home

df_home = df_inv[df_inv["ParkCode"] == "HOME"]

df_home["LatitudeInDecimalDegrees"].plot.hist()
plt.xlabel("Latitude")
plt.ylabel("Frequency")
plt.title("Error Detection")
plt.show()

df_home["LongitudeInDecimalDegrees"].plot.hist()
plt.xlabel("Longitude")
plt.ylabel("Frequency")
plt.title("Error Detection")
plt.show()

df_hosp = df_inv[df_inv["ParkCode"] == "HOSP"]

df_hosp["LatitudeInDecimalDegrees"].plot.hist()
plt.xlabel("Latitude")
plt.ylabel("Frequency")
plt.title("Error Detection")
plt.show()

df_hosp["LongitudeInDecimalDegrees"].plot.hist()
plt.xlabel("Longitude")
plt.ylabel("Frequency")
plt.title("Error Detection")
plt.show()



































# set option to display all data
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)


# load data

df_pub = pd.read_csv("HTLN_InvasivePlants_Monitoring.csv")
df_hosp = pd.read_csv("HospInpCenterPts_corr.csv")
df_home = pd.read_csv("HomeInpCenterPts_corr.csv")

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


# this script is fixing hosp and home <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# complete this and test in Power BI
# if its good, reload published csv and filter out old
# home and hosp and insert new home and hosp

# left join df_pub on df_hosp and df_  

result = df1.merge(df2, on='team', how='left')



    



# Select the 'Name' and 'City' columns
selected_columns = df[['Name', 'City']]

print(selected_columns)



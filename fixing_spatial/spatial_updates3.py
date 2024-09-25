

###############################################################
#
#   spatial_updates3.py
#   importing new thru 2022
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

df_spatial = pd.concat([df_arpo, df_cuva, df_efmo, df_gwca], ignore_index=True)
df_spatial = pd.concat([df_spatial, df_heho, df_hocu, df_home, df_hosp], ignore_index=True)
df_spatial = pd.concat([df_spatial, df_libo, df_peri, df_pipe, df_tapr, df_wicr], ignore_index=True)

# load field data

df_data = pd.read_csv("qryexp_FieldData.csv")


# Perform an inner join - need inner join to omit any mismatches

df_all = df_spatial.merge(df_data, on='LocationID', how='inner')

# include sample year

df_all['SampleYear'] = pd.to_numeric(df_all['PeriodID'].str[10:14])

# write to file

df_all.to_csv("invasive_plants_thru2022.csv", sep=',', encoding='utf-8')






import pandas as pd

df_sheet1 = pd.read_excel('/Users/riyabhandari/Desktop/datacenters_energyputput.xlsx', sheet_name = 'Datacenters')
df_sheet2 = pd.read_excel('/Users/riyabhandari/Desktop/datacenters_energyputput.xlsx', sheet_name = 'Utility')
df_sheet3 = pd.read_excel('/Users/riyabhandari/Desktop/datacenters_energyputput.xlsx', sheet_name = 'EmissionIntensity')

#Adding a dictinoary of all utilities as per different cities
utility = {}
for _, row in df_sheet2.iterrows():
    utility[row['City']] = row['Primary Electric Utility']

#Adding new column of utility in the main datacenters sheet
df_sheet1['Utility'] = df_sheet1['Location'].map(utility)

#Adding Emission intensity in the main sheet
EmissionIntensity ={}

for _, row in df_sheet3.iterrows():
    EmissionIntensity[row['Utility']] = row['Emission Intensity (kg CO₂e/MWh)']

df_sheet1['Emission_intensity (kgCO2/MWh)'] = df_sheet1['Utility'].map(EmissionIntensity)

#Calculating total emissions per datacenters

df_sheet1['Emissions kgCO2'] = df_sheet1['Emission_intensity (kgCO2/MWh)']*df_sheet1['EnergyOutput_Mwh']

#Converting into excel

df_sheet1.to_excel('/Users/riyabhandari/Desktop/datacenters_final.xlsx')
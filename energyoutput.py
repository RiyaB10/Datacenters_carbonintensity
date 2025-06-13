# #Datacenters
# import pandas as pd

# # Load the Excel file
# df = pd.read_excel('/Users/riyabhandari/Desktop/datacenters_capacity.xlsx')

# utilization_factor = 0.67
# running_hours = 8760

# def calculate_energy_output(row):
#     return row['Capacity_mw']*utilization_factor*running_hours
    

# df['EnergyOutput_mwh'] = df.apply(calculate_energy_output, axis=1)

# df.to_excel('/Users/riyabhandari/Desktop/datacenters_energyputput.xlsx', index=False)




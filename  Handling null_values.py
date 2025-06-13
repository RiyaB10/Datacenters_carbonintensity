#Datacenters
import pandas as pd

# Load the Excel file
df = pd.read_excel('/Users/riyabhandari/Downloads/datacenters.xlsx')


# Filter out entries where Capacity_mw > 0 and calculate company average
non_zero_df = df[df['Capacity_mw'] > 0]
company_avg = non_zero_df.groupby('Company')['Capacity_mw'].mean()

# Define a function to apply the replacement
def replace_with_company_avg(row):
    if row['Capacity_mw'] == 0:
        return company_avg.get(row['Company'], 0)  # fallback 0 if company not found
    return row['Capacity_mw']

# Apply the function row-by-row
df['Capacity_mw'] = df.apply(replace_with_company_avg, axis=1)

# Save to a new Excel file
df.to_excel('/Users/riyabhandari/Desktop/imputed_datacenters.xlsx', index=False)

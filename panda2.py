import pandas as pd

# 1. Reading from an Excel file
# Create a sample Excel file
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
df.to_excel('sample.xlsx', index=False)

# Read the created Excel file
df_read = pd.read_excel('sample.xlsx')
print("Reading from Excel file:")
print(df_read)
print()

# 2. Writing to an Excel file
new_data = {
    'Name': ['David', 'Eve'],
    'Age': [28, 22],
    'City': ['San Francisco', 'Boston']
}
df_new = pd.DataFrame(new_data)

# Write the new DataFrame to a new Excel file
df_new.to_excel('new_sample.xlsx', index=False)
print("Written new data to 'new_sample.xlsx'")
print()

# 3. Appending data to an existing Excel file
with pd.ExcelWriter('sample.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
    df_new.to_excel(writer, index=False, header=False, startrow=len(df_read) + 1, sheet_name='Sheet1')

# Read the updated 'sample.xlsx' file to verify the append operation
df_updated = pd.read_excel('sample.xlsx')
print("Updated 'sample.xlsx' with appended data:")
print(df_updated)

# # import pandas as pd


# # df = pd.read_csv(r"customers.csv")
# #df.head()



# import pandas as pd

# # Provide the correct file path to your CSV file
# file_path = r"customers.csv"

# # Use pd.read_csv() to read the CSV file into a DataFrame
# df = pd.read_csv("customers.csv")

# # Display the first few rows of the DataFrame
# print(df.head())


import pandas as pd

# Provide the correct file path to your CSV file
file_path = r"C:\Users\abhay\Downloads\customers-100.csv"

# Use pd.read_csv() to read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

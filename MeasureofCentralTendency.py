import pandas as pd 

# Load the CSV file
csv_file = "energy (1)2008.csv"
data = pd.read_csv(csv_file)

# Print the first few rows to inspect the data
print("Data Preview:\n", data.head())

# Check column names
print("Column Names:\n", data.columns)

# Select numerical columns manually (replace with actual column names)
numerical_columns = ['Column1', 'Column2', 'Column3']  # Example column names
numerical_data = data[numerical_columns]

# Handle missing data (optional)
numerical_data = numerical_data.dropna()  # Or use fillna() to handle NaNs

# Central tendency: mean, median, mode 
mean_values = numerical_data.mean()
median_values = numerical_data.median()
mode_values = numerical_data.mode()

# Print mode values to check
print("Mode Values:\n", mode_values)

# Check if mode_values is empty
if not mode_values.empty:
    mode_values = mode_values.iloc[0]
else:
    mode_values = "No mode found"

print("Mean:\n\n", mean_values, "\n")
print("Median:\n\n", median_values, "\n")
print("Mode:\n\n", mode_values, "\n")
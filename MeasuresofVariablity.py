import pandas as pd

# Load the CSV file
csv_file = "energy (1)2008.csv"
data = pd.read_csv(csv_file)

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values:\n", missing_values, "\n")

# Drop columns where more than 50% of values are missing
threshold = len(data) * 0.5
data = data.dropna(axis=1, thresh=threshold)

# Handle missing values in remaining columns by imputing with mean for numeric and mode for non-numeric
numeric_columns = data.select_dtypes(include=['float64', 'int64', 'float32', 'int32']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

non_numeric_columns = data.select_dtypes(exclude=['float64', 'int64', 'float32', 'int32']).columns
for col in non_numeric_columns:
    data[col] = data[col].fillna(data[col].mode()[0])

# Display the cleaned dataset structure
print("Cleaned dataset structure:\n", data.info(), "\n")

# Select numeric columns only
numeric_data = data.select_dtypes(include=['float64', 'int64', 'float32', 'int32'])

# Check for columns with little to no variability
low_variability_columns = [col for col in numeric_data.columns if numeric_data[col].nunique() <= 1]
if low_variability_columns:
    print("Columns with little to no variability:\n", low_variability_columns, "\n")
    numeric_data = numeric_data.drop(columns=low_variability_columns)

# Calculate variance and standard deviation for the remaining numeric columns
if not numeric_data.empty:
    variance = numeric_data.var()
    std_dev = numeric_data.std()

    print("Variance:\n", variance, "\n")
    print("Standard Deviation:\n", std_dev, "\n")
else:
    print("No numeric data available after preprocessing.\n")

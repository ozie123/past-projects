import pandas as pd

# Load the dataset
file_path = r"\Users\talib\Downloads\New folder\energy (1)2008.csv"
df = pd.read_csv(file_path)

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

# Drop rows with any missing values (NA)
df_no_missing_any = df.dropna(how="any")

# Drop rows where all values are missing (NA)
df_no_missing_all = df.dropna(how="all")

# Display the results for verification
print("Original DataFrame Shape:", df.shape)
print("After Removing Duplicates:", df_no_duplicates.shape)
print("After Dropping Rows with Any Missing Values:", df_no_missing_any.shape)
print("After Dropping Rows with All Missing Values:", df_no_missing_all.shape)

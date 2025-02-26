
import pandas as pd

# Load the dataset
file_path = r"C:\Users\talib\Downloads\New folder\energy (1)2008.csv"
df = pd.read_csv(file_path)

# Display the first few rows for inspection
print("Original Dataset:")
print(df.head())

# Clean and rename columns for ease of use (example: rename unnamed columns)
df.columns = [col.strip().replace("\n", " ").replace(" ", "_").lower() for col in df.columns]

# Drop completely blank rows and columns
df = df.dropna(how="all", axis=0)  # Rows
df = df.dropna(how="all", axis=1)  # Columns

# Example: Sorting by a percentage column (replace 'percentage_column_name' with actual column)
sorted_df = df.sort_values(by="Heating", ascending=False)

# Example: Filtering rows where percentage is greater than 50%
filtered_df = df[df["Heating"] > 50]

# Display the sorted and filtered data
print("\nSorted Data by Percentage:")
print(sorted_df)

print("\nFiltered Data (Percentage > 50):")
print(filtered_df)


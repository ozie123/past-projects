import pandas as pd 
import matplotlib.pyplot as pit

#open the csv file 
csv_file = "energy (1)2008.csv"
data = pd.read_csv(csv_file)

#selects numerical columns
numerical_data = data.select_dtypes(include=['float64' ,' int64'])

#plots histograms 
for column in numerical_data.columns[:12]:
    pit.figure(figsize=(6.4))
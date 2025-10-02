import pandas as pd


# data1.csv: CSV file encoded in CP-1252
# data2.csv: CSV file encoded in UTF-8
# data3.txt: Tab-separated file encoded in UTF-16

data1 = pd.read_csv("data1.csv", encoding="windows-1252")
data2 = pd.read_csv("data2.csv", encoding="utf-8")
data3 = pd.read_csv("data3.txt", sep="\t", encoding="utf-16")

# Combine the dataframes
combined_data = pd.concat([data1, data2, data3], ignore_index=True)

symbols = ["™", "€", "Ž"]

total_value = combined_data[combined_data["symbol"].isin(symbols)]["value"].sum()

print(f"The sum of values for the symbols {symbols} is: {total_value}")

import pandas as pd
from pathlib import Path

csv_files = Path(".").glob("daily_sales_data_*.csv")

# files = [
#     "data/daily_sales_data_0.csv",
#     "data/daily_sales_data_1.csv",
#     "data/daily_sales_data_2.csv"
# ]

dataframes = []

for file in csv_files:
    df = pd.read_csv(file)

    df = df[df['product'] == 'pink morsel']

    df['sales'] = df['quantity'] * df['price']

    df = df[['sales','date','region']]

    dataframes.append(df)

    final_df = pd.concat(dataframes, ignore_index=True)

    final_df.to_csv("formatted_output.csv", index=False)

    print("formatted_output.csv created successfully!")



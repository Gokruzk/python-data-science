# Loading Data with Pandas

import pandas as pd


def run():
    csv_path = "files.csv"
    df = pd.read_csv(csv_path)

    # TODO: print the first 5 rows of the file
    # print(df.head())

    x = df[["Username"]]
    print(x)
    print(df[0,"Username"])

run()

# Loading Data with Pandas

import pandas as pd


def run():
    csv_path = "./files.csv"
    df = pd.read_csv(csv_path)

    # TODO: print the first 5 rows of the file
    # print(df.head())

    # TODO: print one column of the file
    x = df[["Username"]]
    # print(x)

    # TODO: print all rows of the file
    print(df.iloc[0:])

    # TODO: print the element in the second row and first column
    print(df.iloc[1, 0])

    # TODO: get num of rows
    num_rows = df.shape[0]
    print(num_rows)



    df = pd.DataFrame(
        {'Names': ["Hermione", "Ron"], 'House': ["Gryfindor", None]})
    print(df.head())


run()

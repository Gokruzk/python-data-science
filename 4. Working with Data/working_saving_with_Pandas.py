# Working with and Saving Data with Pandas

import pandas as pd


def main():
    students = {
        'Names': ["Hermione", "Ron"],
        'House': ["Gryfindor", "Gryfindor"]
    }
    df = pd.DataFrame(students)
    print(df["House"].unique())

    csv_path = "./files.csv"
    df = pd.read_csv(csv_path)

    # TODO: print the elements which have an Identifier > 5000
    df1 = df[df["Identifier"] > 5000]
    df1.to_csv("new.csv")
    print(df1)

if __name__ == "__main__":
    main()

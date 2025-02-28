import os

import matplotlib
import pandas as pd

if __name__ == "__main__":
    data = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "heart.csv"))
    df = pd.read_csv(data)
    print(df.to_string())  # Print the full dataframe

    # Renaming columns
    df = df.rename(
        columns={
            "cp": "chest_pain",
            "trestbps": "blood_pressure",
            "fbs": "blood_sugar",
            "ca": "vessels",
            "chol": "cholesterol",
        }
    )

    # Creating the 'health_status' column based on target values
    df["health_status"] = df["target"].apply(lambda x: "well" if x == 0 else "unwell")

    # Creating the 'gender' column based on sex values
    df["gender"] = df["sex"].apply(lambda x: "F" if x == 0 else "M")

    # Print the first few rows
    print(df.head())

    # Print the last few rows
    print(df.tail())

    # Get the shape of the DataFrame
    print("Shape of DataFrame:", df.shape)

    # Describe the DataFrame
    print("Description of DataFrame:\n", df.describe())

    # Print any duplicated rows
    print("Duplicated Rows:\n", df[df.duplicated(keep=False)])

    # Print value counts for the 'health_status' column
    print("Health Status Counts:\n", df["health_status"].value_counts())

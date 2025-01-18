import os
import pandas as pd
import matplotlib as plt

if __name__ == "__main__":
    data = os.path.join('..', 'data', "heart.csv")
    df = pd.read_csv(data)
    print(df.to_string())
    data_array = [row.tolist() for index, row in df.iterrows()]

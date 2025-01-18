import pandas as pd
import matplotlib as plt

if __name__ == "__main__":
    df = pd.read_csv("heart.csv")
    print(df.to_string())
    data_array = [row.tolist() for index, row in df.iterrows()]
    fig = plt.figure(figsize = (15,15))

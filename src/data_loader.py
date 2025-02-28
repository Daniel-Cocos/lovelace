import os
import pandas as pd


def load_data():
    data_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "heart.csv")
    )
    df = pd.read_csv(data_path)
    return df

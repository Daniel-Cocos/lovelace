import pandas as pd

def rename_columns(df):
    df = df.rename(columns={
        "cp": "chest_pain",
        "trestbps": "blood_pressure",
        "fbs": "blood_sugar",
        "ca": "vessels",
        "chol": "cholesterol"
    })
    return df

def handle_missing_values(df):
    print("Missing Values:\n", df.isnull().sum())
    df.fillna(df.mean(), inplace=True)
    return df

def create_additional_columns(df):
    df["health_status"] = df["target"].apply(lambda x: "well" if x == 0 else "unwell")
    df["gender"] = df["sex"].apply(lambda x: "F" if x == 0 else "M")
    return df

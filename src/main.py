import os
import pandas as pd
import matplotlib as plt

if __name__ == "__main__":
    data = os.path.join('..', 'data', "heart.csv")
    df = pd.read_csv(data)
    print(df.to_string())
    data_array = [row.tolist() for index, row in df.iterrows()]

heart = heart.rename(columns={"cp": "chest_pain", "trestbps": "blood_pressure", "fbs": "blood_sugar", "ca": "vessels", "chol": "cholesterol"})
heart['health_status'] = heart['target']
heart['health_status'] = ["well" if x == 0 else "unwell" for x in heart['health_status']]
heart['gender'] = heart['sex']
heart['gender'] = ['F' if x == 0 else 'M' for x in heart['gender']]
heart.head()

heart.tail()

heart.shape

heart.describe()

heart[heart.duplicated(keep=False)]


heart['health_status'].value_counts()

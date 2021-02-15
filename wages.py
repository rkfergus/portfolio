import pandas as pd

df = pd.DataFrame()


def load():
    global df
    df = pd.read_csv('static/resources/hours.csv')

    for col in df.columns:
        if 'Unnamed' in col:
            df = df.drop(columns=[col])

    for col in df.columns[1:]:
        print(df[col])
        df[col] = df[col].astype(float)

    return df


def get_averages():
    global df
    return df.describe()
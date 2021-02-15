import pandas as pd

df = pd.DataFrame()


def load():
    global df
    df = pd.read_csv('static/resources/hours.csv')

    for col in df.columns:
        if 'Unnamed' in col:
            df = df.drop(columns=[col])

    return df

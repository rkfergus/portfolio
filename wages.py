import pandas as pd
import plotly as plt


df = pd.DataFrame()


def load():
    global df
    df = pd.read_csv('static/resources/hours.csv')

    for col in df.columns:
        if 'Unnamed' in col:
            df = df.drop(columns=[col])

    # df['Date'] = pd.to_datetime(df['Date'], format())
    # for col in df.columns[3:]:
    #     print(df[col])
    #     df[col] = df[col].astype(float)

    return df


def plot_days(df):
    graph = [dict(data=[
                dict(
                    x=[1, 3, 5],
                    y=[10, 50, 30],
                    type='bar'
                ),
            ],
            layout=dict(
                title='second graph'
            ))]
    return graph[0]

def get_average_by_day():
    # average hours, hourly, and tip out for server shifts
    server_df = df[df['Type'] == 'Server']
    return server_df.groupby('Day').mean()
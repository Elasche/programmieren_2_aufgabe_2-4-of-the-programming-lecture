import pandas as pd
import numpy as np
import plotly.express as px


def read_data():

    df = pd.read_csv("data/activities/activity.csv")

    return df


def add_time(df):

    df["time"] = np.arange(len(df))

    return df


def find_best_effort(power, window_size, sample_duration):

    samples_per_window = int(window_size / sample_duration)

    avg_power = pd.Series(power).rolling(window=samples_per_window).mean().max()

    return {"time": window_size, "avg_power": avg_power}


def create_pc_df(power, sample_duration, window_list):

    results = []

    for window_size in window_list:
        results.append(find_best_effort(power, window_size, sample_duration))

    return pd.DataFrame(results)


def plot_pc(df_pc):

    fig = px.line(df_pc, x="time", y="avg_power", markers=True)

    fig.update_xaxes(
        type="log",
        tickvals=[1, 5, 10, 30, 60, 300, 600, 1200, 1800],
        ticktext=["1s", "5s", "10s", "30s", "1min", "5min", "10min", "20min", "30min"],
    )

    fig.update_layout(xaxis_title="Time", yaxis_title="Power in W")

    return fig


if __name__ == "__main__":
    df = read_data()

    power = df["PowerOriginal"]

    sample_duration = 1

    df = add_time(df)

    window_list = range(30, 1801)  # [10, 20, 30, 60, 300, 600, 1200, 1800]

    df_pc = create_pc_df(power, sample_duration, window_list)

    fig = plot_pc(df_pc)

    fig.show()

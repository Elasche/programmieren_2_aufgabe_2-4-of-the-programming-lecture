import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st


def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV", "Zeit in ms"]

    # Gibt den geladen Dataframe zurück
    return df


def read_my_activity():

    df = pd.read_csv("data/activities/activity.csv")

    N = len(df["PowerOriginal"])

    df["time_secounds"] = np.arange(N)
    df["time_minutes"] = df["time_secounds"] / 60

    return df  # dataframe with the activity


def generating_max_hr(df):

    default_hr = int(df["HeartRate"].max())

    max_hr = st.number_input("Maximale Herzfrequenz", min_value=100, max_value=250, value=default_hr)

    return max_hr


def make_power_hr_plot(df, max_hr):

    # Berechnung der HR Zonen anhand der MaxHR
    zone_1 = max_hr * 0.5
    zone_2 = max_hr * 0.7
    zone_3 = max_hr * 0.8
    zone_4 = max_hr * 0.9
    zone_5 = max_hr

    fig = px.line(
        df, x="time_secounds", y=["PowerOriginal", "HeartRate"], color_discrete_sequence=["#C084FC", "#EF4444"]
    )
    # Zone 1
    fig.add_hrect(y0=0, y1=zone_1, fillcolor="lightblue", opacity=0.2, line_width=0, annotation_text="Zone 1")

    # Zone 2
    fig.add_hrect(y0=zone_1, y1=zone_2, fillcolor="green", opacity=0.2, line_width=0, annotation_text="Zone 2")

    # Zone 3
    fig.add_hrect(y0=zone_2, y1=zone_3, fillcolor="yellow", opacity=0.2, line_width=0, annotation_text="Zone 3")

    # Zone 4
    fig.add_hrect(y0=zone_3, y1=zone_4, fillcolor="orange", opacity=0.2, line_width=0, annotation_text="Zone 4")

    # Zone 5
    fig.add_hrect(y0=zone_4, y1=zone_5, fillcolor="red", opacity=0.2, line_width=0, annotation_text="Zone 5")

    fig.update_layout(showlegend=False, yaxis_title=None, xaxis_title="Time in seconds")

    return fig


def zone_bar_plot(df, max_hr):

    # Berechnung der HR Zonen anhand der MaxHR
    zone_1 = max_hr * 0.5
    zone_2 = max_hr * 0.7
    zone_3 = max_hr * 0.8
    zone_4 = max_hr * 0.9
    zone_5 = max_hr

    z1 = ((df["HeartRate"] >= 0) & (df["HeartRate"] < zone_1)).sum()

    z1_avg_power = df.loc[(df["HeartRate"] >= 0) & (df["HeartRate"] < zone_1), "PowerOriginal"].mean()

    z2 = ((df["HeartRate"] >= zone_1) & (df["HeartRate"] < zone_2)).sum()

    z2_avg_power = df.loc[(df["HeartRate"] >= zone_1) & (df["HeartRate"] < zone_2), "PowerOriginal"].mean()

    z3 = ((df["HeartRate"] >= zone_2) & (df["HeartRate"] < zone_3)).sum()

    z3_avg_power = df.loc[(df["HeartRate"] >= zone_2) & (df["HeartRate"] < zone_3), "PowerOriginal"].mean()

    z4 = ((df["HeartRate"] >= zone_3) & (df["HeartRate"] < zone_4)).sum()

    z4_avg_power = df.loc[(df["HeartRate"] >= zone_3) & (df["HeartRate"] < zone_4), "PowerOriginal"].mean()

    z5 = (df["HeartRate"] >= zone_4).sum()

    z5_avg_power = df.loc[df["HeartRate"] >= zone_4, "PowerOriginal"].mean()

    # angezeigten werte im Balkendiagramm
    zone_df = pd.DataFrame(
        {
            "Zone": ["Zone 5", "Zone 4", "Zone 3", "Zone 2", "Zone 1"],
            "Wert": [z5, z4, z3, z2, z1],
            "Leistung": [z5_avg_power, z4_avg_power, z3_avg_power, z2_avg_power, z1_avg_power],
        }
    )

    zone_df["Leistung"] = zone_df["Leistung"].fillna(0)

    zone_df["Text"] = "<b>" + zone_df["Leistung"].round(0).astype(int).astype(str) + " W</b>"

    # Anzeigen des Balkendiagramms
    fig = px.bar(
        zone_df,
        x="Wert",
        y="Zone",
        orientation="h",
        text="Text",
        color="Zone",
        color_discrete_map={
            "Zone 1": "#ffcccc",
            "Zone 2": "#ff9999",
            "Zone 3": "#ff6666",
            "Zone 4": "#ff3333",
            "Zone 5": "#cc0000",
        },
        title="Zeit in den Herzfrequenz-Zonen",
    )

    fig.update_traces(textposition="inside", textfont_size=14)

    fig.update_layout(showlegend=False, yaxis_title=None, xaxis_title="Time in seconds")

    return fig


def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x="Zeit in ms", y="Messwerte in mV")
    return fig


if __name__ == "__main__":
    activity_df = read_my_activity()

    max_hr = generating_max_hr(activity_df)
    st.write(max_hr)

    my_fig = make_power_hr_plot(activity_df, max_hr)
    bar_HR_zone = zone_bar_plot(activity_df, max_hr)

    # st.plotly_chart(my_fig)
    # st.plotly_chart(bar_HR_zone)

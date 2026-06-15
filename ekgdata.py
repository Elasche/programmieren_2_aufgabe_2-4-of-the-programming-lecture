import json
import pandas as pd
import plotly.express as px

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

    ## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]


        self.df = pd.read_csv(
            self.data, 
            sep='\t', 
            header=None, 
            names=['Messwerte in mV','Zeit in ms']
            )

        self.df = self.df.iloc[:5000]  # Entferne die erste Zeile, da sie nur die Spaltennamen enthält

        self.peaks = pd.DataFrame()
        self.avg_hr = None

    #########################################
    # @staticmethod
    # def load_by_id():
    #     file = open("data/person_da.json")
    #     person_data = json.load(file)

    #     for person_dict in person_data:
    #         print(person)
    #         for ekg_test in person["ekg_tests"]:
    #             return EKGdata(ekg_dict)      
    #     return None

    @classmethod
    def load_by_id(cls, test_id):

        with open("data/person_db.json") as file:
            person_data = json.load(file)

        for person in person_data:
            for ekg_dict in person["ekg_tests"]:
                if ekg_dict["id"] == test_id:
                    return cls(ekg_dict)

        raise ValueError(           
            f"EKG-Test mit ID {test_id} nicht gefunden."
        )

    def find_peaks(self):
        df = self.df.copy()

        window_ms = 150          # kleinere Fenstergröße = bessere Peak-Position
        refractory_ms = 250      # kein Peak schneller als 250 ms
        amplitude_threshold = 350  # Option A: feste Schwelle

        df["is_peak"] = False

        t_min = df["Zeit in ms"].min()
        t_max = df["Zeit in ms"].max()

        peaks = []
        last_peak_time = None

        t = t_min
        while t < t_max:
            block = df[(df["Zeit in ms"] >= t) & (df["Zeit in ms"] < t + window_ms)]

            if len(block) > 0:
                block_max = block["Messwerte in mV"].max()

                if block_max > amplitude_threshold:
                    idx = block["Messwerte in mV"].idxmax()
                    peak_time = df.loc[idx, "Zeit in ms"]

                    if last_peak_time is None or (peak_time - last_peak_time) > refractory_ms:
                        peaks.append(idx)
                        last_peak_time = peak_time

            t += window_ms

        df.loc[:, "is_peak"] = False
        df.loc[peaks, "is_peak"] = True

        self.df = df
        self.peaks = df[df["is_peak"]]

        print(f"{len(self.peaks)} Peaks > {amplitude_threshold} mV gefunden.")

    ###################################################

    def calculate_avg_hr(self):

        if "is_peak" not in self.df.columns:
            raise ValueError(
                "Bitte zuerst find_peaks() ausführen."
        )

        df = self.df.copy()

        df_peaks = df.loc[df["is_peak"]]


        if len(df_peaks) < 2:                      
            return None

        anzahl_peaks = df["is_peak"].sum()

        df_peaks = df.loc[df["is_peak"]]
        df_peaks.head()

        dt_ms = df_peaks["Zeit in ms"].iloc[-1] - df_peaks["Zeit in ms"].iloc[0]
        dt_mins = dt_ms / (60*1000)


        avg_hr = anzahl_peaks / dt_mins            

        self.avg_hr = avg_hr                       

        return avg_hr



    def plot_time_series(self, n_points=2000):

        df_plot = self.df.iloc[:n_points]

        fig = px.line(
            df_plot,
            x="Zeit in ms",
            y="Messwerte in mV",
            title=f"EKG-Test ID: {self.id}" 
        )

        if self.peaks is not None and not self.peaks.empty:

            t_min = df_plot["Zeit in ms"].min()
            t_max = df_plot["Zeit in ms"].max()

            visible_peaks = self.peaks[
                (self.peaks["Zeit in ms"] >= t_min)
                & (self.peaks["Zeit in ms"] <= t_max)
            ]

            fig.add_scatter(
                x=visible_peaks["Zeit in ms"],
                y=visible_peaks["Messwerte in mV"],
                mode="markers",
                name="Peaks",
                marker=dict(
                    color="red",
                    size=10,
                    symbol="circle"
                )
            )

        return fig
    
        # # WICHTIG: Streamlit statt fig.show()
        # import streamlit as st
        # st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())

    print("--- Modul-Test gestartet ---")


    try:
        ekg = EKGdata.load_by_id(test_id=2)

        ekg.find_peaks()

        hr = ekg.calculate_avg_hr()

        print(
            f"Durchschnittliche Herzfrequenz: "
            f"{hr:.1f} bpm"
        )

        ekg.plot_time_series()

    except Exception as e:
        print(f"Fehler im Ablauf: {e}")

# programmieren_2_aufgabe_2-4-of-the-programming-lecture
This repository is used for exercise 2-4

# EKG App – Interaktiver Power & HR Plot

Diese Streamlit-App dient zur Analyse von EKG- und Leistungsdaten verschiedener Versuchspersonen.

## Die Anwendung ermöglicht:
- Auswahl einer Versuchsperson
- Anzeige eines zugehörigen Profilbildes
- Visualisierung von Leistungsdaten (Power & Heart Rate)
- Darstellung von Herzfrequenz-Zonen zur Trainingsanalyse



## Das Projekt wurde in **Python** entwickelt und basiert auf:

- Streamlit (Web-App Interface)
- Plotly (interaktive Visualisierung)
- Pandas (Datenverarbeitung)
- Pillow (Bildverarbeitung)
- PDM als Paket-Manager

---

## Projektstruktur vereinfacht:

- `main.py` → Startpunkt der Streamlit-App
- `read_data.py` → Laden von Personendaten & Bildern
- `read_pandas.py` → Erstellung der Plots
- `data/` → EKG- und Messdaten

---

## Installation & Start (mit PDM)

Dieses Projekt verwendet **PDM (Python Development Master)** als Paketmanager.

### 1. Abhängigkeiten installieren

```bash
pdm install
```

#Leistungskurve II Abgabe 4

es muss folgendes dokument ausfegrührt werden
##advanced_powercurve

Dieses Projekt erstellt eine Power Curve (Leistungskurve) auf Basis von Leistungsdaten in Watt.

Für verschiedene Zeitfenster wird die maximale durchschnittliche Leistung berechnet und anschließend als Diagramm dargestellt.

Die Eingabedaten werden aus einer CSV-Datei eingelesen. Die Ausgabe besteht aus:
- einem DataFrame mit Zeit und Leistung
- einer grafischen Darstellung der Power Curve


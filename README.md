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

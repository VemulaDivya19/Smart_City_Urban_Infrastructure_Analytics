"""
loader.py
---------------------------
Loads Smart City GIS Excel data
"""

import pandas as pd
from pathlib import Path


# Project Root Folder
project_root = Path(__file__).resolve().parent.parent

# Excel Folder
excel_folder = project_root / "Data" / "Excel_Data"


def load_data():
    """Load all infrastructure Excel files"""

    hospitals = pd.read_excel(excel_folder / "Hospitals.xlsx")
    schools = pd.read_excel(excel_folder / "Schools.xlsx")
    water_tanks = pd.read_excel(excel_folder / "Water_Tanks.xlsx")
    bus_stops = pd.read_excel(excel_folder / "Bus_Stops.xlsx")
    traffic_signals = pd.read_excel(excel_folder / "Traffic_Signals.xlsx")

    return {
        "Hospitals": hospitals,
        "Schools": schools,
        "Water_Tanks": water_tanks,
        "Bus_Stops": bus_stops,
        "Traffic_Signals": traffic_signals,
    }


if __name__ == "__main__":

    data = load_data()

    print("\n===================================")
    print(" SMART CITY GIS PROJECT")
    print(" Infrastructure Data Loaded")
    print("===================================\n")

    for layer_name, df in data.items():
        print(f"{layer_name:<20}: {len(df)} records loaded")

    print("\nAll Excel files loaded successfully.")
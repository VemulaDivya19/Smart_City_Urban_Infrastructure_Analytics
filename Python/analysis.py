"""
analysis.py
--------------------------------
Smart City GIS Infrastructure Analysis

This module:
1. Analyzes GIS infrastructure datasets
2. Generates an infrastructure summary
3. Exports the summary to Excel
"""

import pandas as pd
from pathlib import Path
from loader import load_data

# -------------------------------------------------
# Project Paths
# -------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

output_folder = project_root / "Output"

# Create Output folder if it doesn't exist
output_folder.mkdir(exist_ok=True)


# -------------------------------------------------
# Infrastructure Summary
# -------------------------------------------------

def infrastructure_summary(data):
    """
    Generate infrastructure summary and export it to Excel.
    """

    summary = {
        "Infrastructure": [
            "Hospitals",
            "Schools",
            "Water Tanks",
            "Bus Stops",
            "Traffic Signals"
        ],
        "Count": [
            len(data["Hospitals"]),
            len(data["Schools"]),
            len(data["Water_Tanks"]),
            len(data["Bus_Stops"]),
            len(data["Traffic_Signals"])
        ]
    }

    summary_df = pd.DataFrame(summary)

    total = summary_df["Count"].sum()

    print("\n===================================")
    print(" SMART CITY ANALYSIS REPORT")
    print("===================================\n")

    for _, row in summary_df.iterrows():
        print(f"{row['Infrastructure']:<20}: {row['Count']}")

    print("-----------------------------------")
    print(f"Total Infrastructure : {total}")
    print("-----------------------------------")

    # Export Summary
    summary_path = output_folder / "Infrastructure_Summary.xlsx"

    summary_df.to_excel(
        summary_path,
        index=False
    )

    print("\nInfrastructure summary exported successfully!")
    print(f"Location : {summary_path}")

    # Return DataFrame for reuse in other modules
    return summary_df


# -------------------------------------------------
# Run Independently
# -------------------------------------------------

if __name__ == "__main__":

    print("\nRunning Infrastructure Analysis...\n")

    data = load_data()

    infrastructure_summary(data)

    print("\nAnalysis Completed Successfully!")
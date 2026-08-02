"""
charts.py
--------------------------------
Generate professional charts for Smart City GIS Project
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project folders
project_root = Path(__file__).resolve().parent.parent
output_folder = project_root / "Output"

summary_file = output_folder / "Infrastructure_Summary.xlsx"

# Read summary
summary = pd.read_excel(summary_file)

# Create Charts folder
charts_folder = output_folder / "Charts"
charts_folder.mkdir(exist_ok=True)


def bar_chart():

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        summary["Infrastructure"],
        summary["Count"]
    )

    # Add values on top of each bar
    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1,
            f"{int(height)}",
            ha="center",
            fontsize=11,
            fontweight="bold"
        )

    plt.title(
        "Smart City Infrastructure Count",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel(
        "Infrastructure",
        fontsize=12
    )

    plt.ylabel(
        "Number of Features",
        fontsize=12
    )

    plt.xticks(
        rotation=15,
        fontsize=11
    )

    plt.yticks(fontsize=11)

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.5
    )

    plt.tight_layout()

    plt.savefig(
        charts_folder / "Infrastructure_BarChart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("✓ Bar Chart Created")


def pie_chart():

    plt.figure(figsize=(8, 8))

    plt.pie(
        summary["Count"],
        labels=summary["Infrastructure"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(
        "Infrastructure Distribution",
        fontsize=16,
        fontweight="bold"
    )

    plt.tight_layout()

    plt.savefig(
        charts_folder / "Infrastructure_PieChart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("✓ Pie Chart Created")


if __name__ == "__main__":

    print("\nGenerating Professional Charts...\n")

    bar_chart()
    pie_chart()

    print("\n======================================")
    print(" Charts Generated Successfully")
    print("======================================")
    print(f"\nLocation : {charts_folder}")
"""
report_generator.py
--------------------------------
Generate a PDF report for the Smart City GIS Project.
"""

from pathlib import Path
import pandas as pd

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)


def generate_report():

    project_root = Path(__file__).resolve().parent.parent

    output_folder = project_root / "Output"

    summary_file = output_folder / "Infrastructure_Summary.xlsx"

    charts_folder = output_folder / "Charts"

    report_file = output_folder / "Smart_City_Report.pdf"

    # Load summary
    summary = pd.read_excel(summary_file)

    # Create PDF
    doc = SimpleDocTemplate(str(report_file))

    styles = getSampleStyleSheet()

    story = []

    # -------------------------------------------------
    # Title
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b><font size=20>Smart City Urban Infrastructure Planning & Analytics Report</font></b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    # -------------------------------------------------
    # Overview
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Project Overview</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "This report summarizes the urban infrastructure available in the Smart City GIS Project. "
            "The analysis was performed using QGIS, Python, Pandas and Matplotlib.",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # -------------------------------------------------
    # Infrastructure Table
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Infrastructure Summary</b>",
            styles["Heading2"]
        )
    )

    data = [["Infrastructure", "Count"]]

    for _, row in summary.iterrows():
        data.append([row["Infrastructure"], row["Count"]])

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ]))

    story.append(table)

    story.append(Spacer(1, 20))

    # -------------------------------------------------
    # Charts
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Infrastructure Charts</b>",
            styles["Heading2"]
        )
    )

    bar_chart = charts_folder / "Infrastructure_BarChart.png"

    pie_chart = charts_folder / "Infrastructure_PieChart.png"

    if bar_chart.exists():
        story.append(Image(str(bar_chart), width=420, height=250))

    story.append(Spacer(1, 15))

    if pie_chart.exists():
        story.append(Image(str(pie_chart), width=320, height=320))

    story.append(Spacer(1, 20))

    # -------------------------------------------------
    # Key Findings
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Key Findings</b>",
            styles["Heading2"]
        )
    )

    total = summary["Count"].sum()

    highest = summary.loc[summary["Count"].idxmax()]
    lowest = summary.loc[summary["Count"].idxmin()]

    findings = f"""
    • Total mapped infrastructure assets: <b>{total}</b><br/><br/>
    • Highest available infrastructure: <b>{highest['Infrastructure']}</b>
      ({highest['Count']})<br/><br/>
    • Lowest available infrastructure: <b>{lowest['Infrastructure']}</b>
      ({lowest['Count']})<br/><br/>
    • This analysis demonstrates the integration of GIS, Python,
      Excel and Data Analytics for smart city planning.
    """

    story.append(
        Paragraph(
            findings,
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # -------------------------------------------------
    # Footer
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Generated Automatically using Python</b>",
            styles["Italic"]
        )
    )

    doc.build(story)

    print("\n=====================================")
    print(" PDF REPORT GENERATED SUCCESSFULLY")
    print("=====================================")
    print(f"\nLocation : {report_file}")


if __name__ == "__main__":
    generate_report()
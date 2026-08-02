"""
main.py
--------------------------------
Smart City Urban Infrastructure Planning & Analytics System

Workflow:
1. Load GIS datasets
2. Generate infrastructure summary
3. Generate charts
4. Generate PDF report
"""

from loader import load_data
from analysis import infrastructure_summary
from charts import bar_chart, pie_chart
from report_generator import generate_report


def main():

    print("\n==============================================")
    print(" SMART CITY URBAN INFRASTRUCTURE ANALYTICS")
    print("==============================================")

    # Step 1
    print("\nStep 1 : Loading GIS Data...")

    data = load_data()

    print("✓ GIS data loaded successfully.")

    # Step 2
    print("\nStep 2 : Performing Infrastructure Analysis...")

    infrastructure_summary(data)

    print("✓ Analysis completed.")

    # Step 3
    print("\nStep 3 : Generating Charts...")

    bar_chart()
    pie_chart()

    print("✓ Charts generated successfully.")

    # Step 4
    print("\nStep 4 : Generating PDF Report...")

    generate_report()

    print("✓ PDF report generated successfully.")

    # Completion
    print("\n==============================================")
    print(" PROJECT COMPLETED SUCCESSFULLY")
    print("==============================================")

    print("\nGenerated Files")

    print("✓ Output/Infrastructure_Summary.xlsx")
    print("✓ Output/Charts/Infrastructure_BarChart.png")
    print("✓ Output/Charts/Infrastructure_PieChart.png")
    print("✓ Output/Smart_City_Report.pdf")

    print("\n==============================================")
    print(" Smart City GIS Project Finished Successfully ")
    print("==============================================")

    print("\nThank you for using the Smart City Urban Infrastructure Planning & Analytics System!")


if __name__ == "__main__":
    main()
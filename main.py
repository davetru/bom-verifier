import pandas as pd
import json
import os
from tkinter import Tk, filedialog

REQUIRED_FIELDS = ["Part Number", "Description", "Value", "Footprint"]
PART_LIBRARY_PATH = "part_library.json"

def load_bom(file_path):
    """Loads a BOM file from .csv or .xlsx format."""
    try:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".xlsx":
            return pd.read_excel(file_path, engine="openpyxl")
        elif ext == ".csv":
            return pd.read_csv(file_path)
        else:
            print(f"Unsupported file type: {ext}")
            return None
    except Exception as e:
        print(f"Error loading BOM: {e}")
        return None

def load_part_library(file_path):
    """Loads the part library from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading part library: {e}")
        return {}

def validate_bom(bom_df, part_library):
    """
    Validates the BOM DataFrame against the part library.
    Returns a list of issues with missing fields or unknown parts.
    """
    errors = []

    for index, row in bom_df.iterrows():
        row_errors = []
        for field in REQUIRED_FIELDS:
            value = row.get(field, "")
            if pd.isna(value) or str(value).strip() == "":
                row_errors.append(f"Missing {field}")

        part_number = str(row.get("Part Number", "")).strip()
        if part_number not in part_library:
            row_errors.append("Part not in library")

        if row_errors:
            errors.append({
                "Row": index + 2,
                "Errors": "; ".join(row_errors)
            })

    return errors

def main():
    """Main function to run BOM validation from a user-selected file."""
    root = Tk()
    root.withdraw()

    print("Please select a BOM file (.csv or .xlsx)...")
    bom_file = filedialog.askopenfilename(
        title="Select BOM File",
        filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")]
    )

    if not bom_file:
        print("No file selected. Exiting.")
        return

    bom = load_bom(bom_file)
    part_library = load_part_library(PART_LIBRARY_PATH)

    if bom is None:
        return

    issues = validate_bom(bom, part_library)

    if issues:
        print("Issues found:")
        for issue in issues:
            print(f"Row {issue['Row']}: {issue['Errors']}")

        report_path = "bom_issues_report.csv"
        pd.DataFrame(issues).to_csv(report_path, index=False)
        print(f"\nReport saved to '{report_path}'")
    else:
        print("BOM is valid.")

if __name__ == "__main__":
    main()

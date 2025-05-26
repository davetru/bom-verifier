import pandas as pd
import json
import os
from tkinter import Tk, filedialog

def convert_parts_to_json(input_file, output_file="part_library.json"):
    """
    Converts a CSV or XLSX parts file to a JSON library for BOM validation.
    """
    ext = os.path.splitext(input_file)[1].lower()

    try:
        if ext == ".csv":
            df = pd.read_csv(input_file)
        elif ext == ".xlsx":
            df = pd.read_excel(input_file, engine="openpyxl")
        else:
            print(f"Unsupported file format: {ext}")
            return

        required_fields = {"Part Number", "Description", "Value", "Footprint"}
        if not required_fields.issubset(df.columns):
            print("❌ Error: Missing one or more required columns in the spreadsheet.")
            return

        part_dict = {}

        for _, row in df.iterrows():
            part_number = str(row.get("Part Number", "")).strip()
            if not part_number:
                continue  # Skip rows with no part number

            part_dict[part_number] = {
                "Description": str(row.get("Description", "")).strip(),
                "Value": str(row.get("Value", "")).strip(),
                "Footprint": str(row.get("Footprint", "")).strip()
            }

        with open(output_file, 'w') as f:
            json.dump(part_dict, f, indent=4)

        print(f"✅ Successfully converted '{input_file}' to '{output_file}'.")

    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Prompts user to select a parts file and converts it to JSON."""
    root = Tk()
    root.withdraw()

    print("Please select a parts file (.csv or .xlsx)...")
    parts_file = filedialog.askopenfilename(
        title="Select Parts File",
        filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")]
    )

    if not parts_file:
        print("No file selected. Exiting.")
        return

    convert_parts_to_json(parts_file)

if __name__ == "__main__":
    main()

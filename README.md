# 🧰 BOM Verifier & Part Library Converter

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/davetru/bom-verifier)
![Repo Size](https://img.shields.io/github/repo-size/davetru/bom-verifier)
![Issues](https://img.shields.io/github/issues/davetru/bom-verifier)

A Python-based toolset to validate Bills of Materials (BOMs) against an approved internal part library, ensuring clean, complete, and ready-for-manufacturing design data.

---

## 🔍 What It Does

This project includes two tools:

### 1. **BOM Verifier (`main.py`)**
- 📂 Allows you to select a BOM file (`.csv` or `.xlsx`)
- ✅ Verifies that all required fields are present and non-empty
- 🔎 Cross-checks part numbers against a known `part_library.json`
- 🧾 Outputs a clear report of any issues to `bom_issues_report.csv`

### 2. **Part Library Converter (`convert-to-json.py`)**
- 📂 Allows you to select a `.csv` or `.xlsx` spreadsheet of parts
- 🔄 Converts it into a properly structured `part_library.json`
- ⚠️ Ensures all required fields are included in the input

---

## 📁 Example Project Structure

```
bom-verifier/
├── main.py
├── convert-to-json.py
├── part_library.json
├── sample_bom.csv
├── bom_issues_report.csv (auto-generated)
├── requirements.txt
└── README.md
```

---

## ✅ Requirements

Make sure you have Python 3.x and install the required packages:

```bash
pip install -r requirements.txt
```

**Or manually install:**

```bash
pip install pandas openpyxl
```

---

## ⚙️ Configuration

You can define which fields are required in `main.py`:

```python
REQUIRED_FIELDS = ["Part Number", "Description", "Value", "Footprint"]
```

Update this list to match your organization’s BOM structure.

---

## 📦 Usage

### 🔍 To Validate a BOM:

```bash
python main.py
```
You'll be prompted to select your `.csv` or `.xlsx` BOM file. If issues are found, a `bom_issues_report.csv` will be generated in the project folder.

---

### 🧱 To Convert a Parts File to JSON:

```bash
python convert-to-json.py
```
Select your spreadsheet file, and it will generate `part_library.json`.

---

## 💼 Why It’s Useful

- ✨ Cross-functional automation between hardware and software
- 💡 Great for ECAD Librarians, hardware engineers, and QA workflows
- 📉 Reduces BOM errors and manual validation overhead

---

## 📜 License

MIT License

---

## 🙋‍♂️ Created By

**Dave Tran**  
💻 [GitHub](https://github.com/davetru) • 📧 [Email](mailto:david@davidtrutran.om)

---

## 🤝 Contributions

Feel free to fork and contribute! Pull requests welcome for:
- Feature additions
- UI improvements
- PLM system integration

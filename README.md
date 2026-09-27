# Clinical Trial Medical Coding & QC Automation Pipeline

## 📌 Project Overview
In Clinical Data Management (CDM), processing free-text Adverse Event (AE) descriptions entered by clinical sites is a high-volume, tedious task. Investigators often use typos, shorthand, and colloquial terms. 

This project simulates an automated **Medical Coding and Quality Control (QC) Pipeline** using Python. It ingests raw clinical data, standardizes text, performs fuzzy-matching against a standardized MedDRA-style dictionary, and automatically categorizes records into auto-coded entries versus flagged queries requiring manual medical review.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Data Manipulation:** `pandas`
* **Algorithm:** `difflib` (Fuzzy string matching)
* **Format:** CSV (for transparent GitHub previewability)

---

## 🔄 Project Workflow
1. **Data Ingestion:** Loads mock Electronic Data Capture (eCRF) raw adverse events and standard dictionary reference tables.
2. **Text Normalization:** Converts investigator text to lowercase and strips formatting variations to prepare for matching.
3. **Fuzzy String Matching:** Evaluates verbatim descriptions against preferred terms using pattern-matching algorithms.
4. **Exception Handling & QC Logic:**
   * **Auto-Coded:** Successfully maps high-confidence matches to their official dictionary codes.
   * **Query Raised / Uncoded:** Flags ambiguous or unrecognized terms for manual medical reviewer intervention.
5. **Audit Report Generation:** Exports a structured compliance log (`medical_coding_report.csv`) for data coordinators.

---

## 📂 Repository Structure
* `raw_aes.csv` — Raw investigator-entered adverse events (input).
* `meddra_dictionary.csv` — Standard medical dictionary reference table (lookup).
* `meddra_coder.py` — The core automation and fuzzy-matching script.
* `medical_coding_report.csv` — The final generated QC audit log (output).

---

## 🚀 How to Run the Script
1. Clone the repository or download the files into your local directory.
2. Ensure you have Python and Pandas installed (`pip install pandas`).
3. Run the script in your terminal:
   ```bash
   python meddra_coder.py

import pandas as pd
from difflib import get_close_matches

print("--- Starting Medical Coding & QC Pipeline ---")

# 1. Load data sources
raw_aes_df = pd.read_csv('raw_aes.csv')
meddra_df = pd.read_csv('meddra_dictionary.csv')

coded_results = []
dictionary_terms = meddra_df['Preferred_Term'].tolist()

# 2. Process each adverse event description
for index, row in raw_aes_df.iterrows():
    subject_id = row['Subject_ID']
    site_id = row['Site_ID']
    raw_desc = str(row['Raw_AE_Description'])
    
    # Normalize text to lowercase for cleaner matching
    cleaned_desc = raw_desc.lower()
    
    # 3. Fuzzy match against dictionary terms
    matches = get_close_matches(cleaned_desc, [term.lower() for term in dictionary_terms], n=1, cutoff=0.3)
    
    if matches:
        matched_lower = matches[0]
        matched_row = meddra_df[meddra_df['Preferred_Term'].str.lower() == matched_lower].iloc[0]
        
        assigned_term = matched_row['Preferred_Term']
        meddra_code = matched_row['Code']
        coding_status = 'Auto-Coded'
    else:
        assigned_term = 'UNRESOLVED - NEEDS MANUAL REVIEW'
        meddra_code = 'N/A'
        coding_status = 'Query Raised / Uncoded'

    # Store the processed result
    coded_results.append({
        'Subject_ID': subject_id,
        'Site_ID': site_id,
        'Raw_AE_Description': raw_desc,
        'Assigned_MedDRA_Term': assigned_term,
        'MedDRA_Code': meddra_code,
        'Coding_Status': coding_status
    })

# 4. Export the audit report
output_df = pd.DataFrame(coded_results)
output_df.to_csv('medical_coding_report.csv', index=False)

print("\nMedical coding process completed successfully!")
print(f"Total records processed: {len(output_df)}")
print("Output report saved to 'medical_coding_report.csv'.")
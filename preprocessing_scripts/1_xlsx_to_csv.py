import pandas as pd

"""
This script reads the excel spreadsheet and writes the two tables that we are interested in, 
    ST9: general patient information
    ST10: patient microbiome counts
to pandas dataframe pickles. The merged dataframe is also 
"""

patient_general = pd.read_excel('../data/raw_data.xlsx', sheet_name='ST9', header=1)
microbiome_counts = pd.read_excel('../data/raw_data.xlsx', sheet_name='ST10', header=1)

patient_general.to_pickle('../data/patient_general_metadata.pkl')
microbiome_counts.to_pickle('../data/microbiome_counts.pkl')

all_data = patient_general.merge(microbiome_counts)
all_data.to_pickle('../data/merged_dataframe.pkl')
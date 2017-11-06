# -------------------- Importing necessary libraries
import pandas as pd
import numpy as np

# -------------------- Reading necessary files with necessary columns
plan_attributes = pd.read_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Plan_Attributes_PP1.csv", encoding="latin")

# -------------------- Checking number of nulls in all columns
print(plan_attributes.isnull().sum(axis=0))

# -------------------- Replacing nulls
replace_missing = {'DiseaseManagementProgramsOffered': "None", 'TEHBInnTier1IndividualMOOP': 0,
                   'TEHBOutOfNetIndividualMOOP': 0, 'TEHBDedInnTier1Individual': 0,
                   'TEHBDedInnTier1Coinsurance': 0, 'TEHBDedOutOfNetIndividual': 0,
                   'URLForEnrollmentPayment': "Unavailable", 'PlanBrochure': "Unavailable",
                   'SpecialistRequiringReferral': "NA"}
plan_attributes = plan_attributes.fillna(replace_missing)

# -------------------- Checking number of nulls in all columns
print(plan_attributes.isnull().sum(axis=0))

# -------------------- Replacing irrelevant information
plan_attributes = plan_attributes.replace('Not Applicable', 0)

for col in ['TEHBInnTier1IndividualMOOP', 'TEHBOutOfNetIndividualMOOP', 'TEHBDedInnTier1Individual',
            'TEHBDedOutOfNetIndividual', 'TEHBDedInnTier1Coinsurance']:
    plan_attributes[col] = plan_attributes[col].replace('[\$,%]', '', regex=True).astype(float).astype(int)

# -------------------- Binning
bin_labels = [0, 1, 2, 3]
bin_IN = [-1, 100, 500, 2000, 100000]
bin_OON = [-1, 100, 1000, 10000, 100000]
bin_coins = [-1, 25, 50, 75, 100]
for col in ['TEHBInnTier1IndividualMOOP', 'TEHBDedInnTier1Individual']:
    plan_attributes[col+"_R"] = pd.cut(plan_attributes[col], bin_IN, labels=bin_labels)
for col in ['TEHBOutOfNetIndividualMOOP', 'TEHBDedOutOfNetIndividual']:
    plan_attributes[col+"_R"] = pd.cut(plan_attributes[col], bin_OON, labels=bin_labels)
plan_attributes['TEHBDedInnTier1Coinsurance_R'] = pd.cut(plan_attributes['TEHBDedInnTier1Coinsurance'], bin_coins,
                                                         labels=bin_labels)

# -------------------- Saving Initial Pre-Processed DF into CSV
plan_attributes.to_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Plan_Attributes_PP2.csv", index=False)
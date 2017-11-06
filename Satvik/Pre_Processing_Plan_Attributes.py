# -------------------- Importing necessary libraries
import pandas as pd

# -------------------- Reading necessary files with necessary columns
plan_attributes = pd.read_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Plan_Attributes_PUF.csv", encoding="latin",
                              usecols=[1,2,5,6,9,12,14,16,17,21,22,23,27,30,36,41,42,43,93,99,133,136,141,151])

# -------------------- Eliminating those plans that don't deal with Individuals
plan_attributes = plan_attributes[plan_attributes['MarketCoverage'] == 'Individual']

# -------------------- Eliminating those plans that are Dental only
plan_attributes = plan_attributes[plan_attributes['DentalOnlyPlan'] == 'No']

# -------------------- Dropping columns 'MarketCoverage', 'DentalOnlyPlan' and 'ChildOnlyOffering'
plan_attributes.drop(['MarketCoverage', 'DentalOnlyPlan', 'ChildOnlyOffering'], axis=1, inplace=True)

# -------------------- Creating a set of programs that are dealt with
disease_programs = plan_attributes['DiseaseManagementProgramsOffered']
programs = set()
for each in disease_programs:
    if not pd.isnull(each):
        programs.update(each.split(", "))

# -------------------- Reordering columns
columns = ['StateCode',
 'IssuerId',
 'PlanId',
 'PlanMarketingName',
 'NetworkId',
 'PlanType',
 'MetalLevel',
 'IsNoticeRequiredForPregnancy',
 'IsReferralRequiredForSpecialist',
 'SpecialistRequiringReferral',
 'DiseaseManagementProgramsOffered',
 'OutOfCountryCoverage',
 'TEHBInnTier1IndividualMOOP',
 'TEHBOutOfNetIndividualMOOP',
 'TEHBDedInnTier1Individual',
 'TEHBDedInnTier1Coinsurance',
 'TEHBDedOutOfNetIndividual',
 'FormularyId',
 'FormularyURL',
 'URLForEnrollmentPayment',
 'PlanBrochure']

plan_attributes = plan_attributes[columns]

# -------------------- Saving Initial Pre-Processed DF into CSV
plan_attributes.to_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Plan_Attributes_PP1.csv", index=False)


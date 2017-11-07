# -------------------- Importing necessary libraries
import pandas as pd

# -------------------- Reading necessary files with necessary columns
df = pd.read_csv('C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\Plans_shortlisted.csv', usecols=[1],
                 header=None)
df1 = pd.read_csv('C:\\Users\\satvi\\Documents\\DDDM\\Project\\Benefits_Cost_Sharing_PUF.csv', usecols=[1,2,5,6,7,8,10,11,13,17,18])

# -------------------- Plans that are non-dental and individual only
plans_list = df[1].tolist()

# -------------------- Removing plans and benefits that are irrelevant
df1 = df1[~df1['BenefitName'].str.contains('Dental')]
df1 = df1[df1['StandardComponentId'].isin(plans_list)]

# -------------------- Saving Pre-Processed DF into CSV
df1.to_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Benefits_Cost_Sharing_PP1.csv", index=False)
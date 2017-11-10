# -------------------- Importing necessary libraries
import pandas as pd
import numpy as np

# -------------------- Reading necessary files with necessary columns
quality = pd.read_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Quality_PUF.csv", encoding="latin",
                              usecols=[0,1,2,3,4,5])

# -------------------- Removing records for which no rating is available
quality = quality[~((quality['GlobalRatingValue'] == 'NR') & (quality['EnrolleeExperienceRatingValue'] == 'NR') &
                  (quality['PlanEfficiencyAffordabilityManagementRatingValue'] == 'NR') &
                  (quality['ClinicalQualityManagementRatingValue'] == 'NR'))]

# -------------------- Fixing column names
cols = ['IssuerID', 'PlanID', 'Global_Rating', 'Enrollee_Experience_Rating', 'Plan_Affordability_Rating',
        'Clinical_Quality_Rating']
quality.columns = cols

# -------------------- Saving Initial Pre-Processed DF into CSV
quality.to_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Quality_Ratings_PP1.csv", index=False)


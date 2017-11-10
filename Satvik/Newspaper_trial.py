'''
This code returns results that contains a figure for insurance plans with information about it retrieved from Google.
A more refined version would include particular keywords from our truth table like deductible, copay, etc.
'''

import newspaper
import google
import pandas as pd
import re

# Different plans as a test
pl = pd.read_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\IssuerID_Name.csv")
issuers = pd.read_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Plan_Attributes_PP2.csv", usecols=[1])
issuer_ids = issuers['IssuerId'].tolist()
pl = pl[pl['IssuerID'].isin(issuer_ids)]
plans = pl['Issuer_Name'].tolist()
idList = pl['IssuerID'].tolist()
plans = [name + ' health insurance reviews' for name in plans]
count = 0
plans_covered = 0

number_of_companies_reviewed = 0
total_companies = 0
indexInPlans = 0;

# f = open( "output.csv" , 'w', encoding="latin")
comments = []

for p in plans[0:3]:
    # f.write(str( idList[indexInPlans] ) + ", ")
    plan_comm = []
    indexInPlans += 1
    total_companies += 1

    search_results = google.search(p, stop=4, lang="en")
    print("*"*30)
    print(p.upper())
    print("_"*15)
    iterated = 0
    for link in search_results:
        if ( ("www.bbb.org" not in link) and ("usinsuranceagents.com" not in link)):
            continue
        try:
            data = newspaper.Article(url=link)
            data.download()
            data.parse()
        except:
            continue

        text = data.text
        linesOfText = text.split('\n')

        if( "usinsuranceagents.com" in link):
            for line in linesOfText:
                if( "found the following review helpful." in line):
                    if (iterated == 0):
                        number_of_companies_reviewed += 1
                        iterated = 1
                    filtered = re.sub("[0-9]+ of [0-9]+ people found the following review helpful.", "", line)
                    filtered = filtered.replace("Help others find the most helpful reviews Was this review helpful to you? Yes | No", "")
                    # filtered = filtered.replace(",", " ")
                    filtered = filtered.replace("\n", ". ")
                    filtered = filtered.replace("\"", " ")
                    filtered = filtered.replace("\'", " ")
                    filtered = filtered.replace("[", " ")
                    filtered = filtered.replace("]", " ")
                    if filtered.strip() != "":
                        plan_comm.append(filtered)
                        print(filtered + '\n')
    comments.append(plan_comm)

df = pd.DataFrame(data={'IssuerID':idList[0:3], 'Reviews':comments})
df.to_csv("Reviews.csv", index=False)
# f.close()
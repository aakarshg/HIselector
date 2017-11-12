'''
This code returns results that contains a figure for insurance plans with information about it retrieved from Google.
A more refined version would include particular keywords from our truth table like deductible, copay, etc.
'''

import newspaper
import google
import pandas as pd
import re
import time
from fake_useragent import UserAgent
ua = UserAgent()

pl = pd.read_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\IssuerID_Name_Updated.csv")
issuers = pd.read_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Plan_Attributes_PP2.csv", usecols=[1])

issuer_ids = issuers['IssuerId'].tolist()
pl = pl[pl['IssuerID'].isin(issuer_ids)]
IssuerName = pl['Issuer_Name'].tolist()
idList = pl['IssuerID'].tolist()
plans = [name + ' usinsuranceagents.com health insurance reviews' for name in IssuerName]
count = 0
comments = []

for p in plans:
    plan_comm = []
    search_results = google.search(p, stop=4, lang="en", pause=3.0, user_agent=ua.random)
    print("*"*30)
    print(p.upper())
    print("_"*15)
    iterated = 0
    for link in search_results:
        if "usinsuranceagents.com" not in link:
            continue
        try:
            data = newspaper.Article(url=link)
            data.download()
            time.sleep(1)
            data.parse()
        except:
            continue

        text = data.text
        # print("Entire text "+ text)
        linesOfText = text.split('\n')
        next_line = False
        for line in linesOfText:
            # if "found the following review helpful." in line:
            if re.search("(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?"
                         "|Oct(ober)?|Nov(ember)?|Dec(ember)?),\s+20\d{2}", line):
                filtered = re.sub("(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?"
                                  "|Oct(ober)?|Nov(ember)?|Dec(ember)?),\s+20\d{2}", "", line)
                filtered = re.sub(r'[0-9]+ of [0-9]+ people found the following review helpful.', "", filtered)
                filtered = filtered.replace("Help others find the most helpful reviews Was this review helpful to you? Yes | No", "")
                filtered = filtered.replace("\n", ". ").replace("\"", "").replace("\'", "").replace("[", " ").\
                    replace("]", " ").strip()
                filtered = re.sub("\s\s+", " ", filtered)
                if filtered.strip() != "" and filtered.strip() != "Health Insurance,":
                    plan_comm.append(filtered.capitalize())
                    print(filtered + '\n')
                iterated += 1
            elif re.search(r'[0-9]+ of [0-9]+ people found the following review helpful.', line):
                next_line = True
            elif next_line and line.strip() != "":
                filtered = re.sub("Help others find the most helpful reviews", "", line)
                filtered = re.sub("\s\s+", " ", filtered)
                filtered = filtered.replace("\n", ". ").replace("\"", "").replace("\'", "").replace("[", " "). \
                    replace("]", " ").strip()
                print(filtered)
                if filtered.strip() != "" and filtered.strip() != 'Health Insurance,':
                    plan_comm.append(filtered.strip())
                iterated += 1
                next_line = False
        if iterated>0:
            break;
    comments.append(plan_comm)
    count += 1
    print(count)
    search_results.close()

review_df = pd.DataFrame(data={'IssuerID': idList, 'IssuerName': IssuerName, 'Reviews': comments})
review_df.to_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Reviews.csv", index=False)
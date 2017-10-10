'''
This code returns results that contains a figure for insurance plans.
A more refined version would include particular keywords from our truth table like deductible, copay, etc.
'''

import newspaper
import google
import re

# Different plans as a test
plans = ['student blue health insurance', 'PSI health insurance', 'ISO health insurance']
for p in plans:
    search_results = google.search(p, stop=4, lang="en")
    print("*"*30)
    print(p.upper())
    print("_"*15)
    for link in search_results:
        data = newspaper.Article(url=link)
        data.download()
        data.parse()
        text = data.text
        for line in text.split(". "):
            match = re.search(r'.*[$].*', line)
            if match:
                print(match.group())
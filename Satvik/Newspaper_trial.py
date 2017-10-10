import newspaper
import google
import re

plans = ['student blue health insurance', 'PSI health insurance', 'ISO health insurance']
for p in plans:
    search_results = google.search(p, stop=4, lang="en")
    print("*"*30)
    for link in search_results:
        data = newspaper.Article(url=link)
        data.download()
        data.parse()
        text = data.text
        for line in text.split(". "):
            match = re.search(r'.*[$].*', line)
            if match:
                print(match.group())
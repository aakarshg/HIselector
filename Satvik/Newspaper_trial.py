import newspaper
import google

search_results = google.search("north carolina health insurance plans", stop=4, lang="en")
print("*"*30)
for link in search_results:
    data = newspaper.Article(url=link)
    data.download()
    data.parse()
    text = data.text #.replace("\n"," ")
    print(text)
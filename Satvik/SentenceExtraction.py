from textblob import TextBlob

data = open("C:\\Users\\satvi\\Documents\\DDDM\\Classwork\\Bag of Words\\Company_Profiles_and_Directories_US_Law_Revi2017-08-24_13-46.txt", encoding='utf-8').read()

bunch = TextBlob(data)

find_good = bunch.sentences

key_words = []
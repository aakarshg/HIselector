import sys
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import nltk
#nltk.download()

data = open("C:\\Users\\satvi\\Documents\\DDDM\\Classwork\\Bag of Words\\Company_Profiles_and_Directories_US_Law_Revi2017-08-24_13-46.txt", encoding='utf-8').read()

words = word_tokenize(data)

# Pre-cleaning
spread = FreqDist(words)
spread.plot(50)
for word,freq in spread.most_common(100):
    print(u'{};{}'.format(word, freq))

# Cleaning
words = [w.lower() for w in words if w.isalpha()]
with open('C:\\Users\\satvi\\Documents\\DDDM\\Classwork\\Bag of Words\\Tokenized_text.txt', 'w', encoding='utf-8') as f:
    print(words, file=f)

stop_words = set(stopwords.words('english'))
words_clean = [w for w in words if w not in stop_words]
common_words = []
for word,freq in spread.most_common(100):
    common_words.append(word)
words_cleaner = [w for w in words_clean if w not in common_words]

# Post-Cleaning
spread = FreqDist(words_cleaner)
spread.plot(50)
with open('C:\\Users\\satvi\\Documents\\DDDM\\Classwork\\Bag of Words\\Ethical_words.txt', 'w', encoding='utf-8') as f:
    for word,freq in spread.most_common(100):
        print(u'{};{}'.format(word, freq))
        print(word, file=f)

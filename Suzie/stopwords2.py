import sys
import io
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

data = open('/Users/susannamoneta/Documents/NCSU/SrSm1/CSC495/Project1/test.txt', encoding='utf-8').read()

words = word_tokenize(data)
words_selected = []
for w in words:
	if w not in stop_words:
		words_selected.append(w)

print(stop_words)

import sys
import io
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def freq_analysis():

	data = open('/Users/susannamoneta/Documents/NCSU/SrSm1/CSC495/Project1/test.txt', encoding='utf-8').read()

	words = word_tokenize(data)

	spread = nltk.FreqDist(words)
	#pread.plot(50,cumulative=True)
	for word, frequency in spread.most_common(100):
		print(u'{};{}'.format(word, frequency))

	return words;


from stopwords import *

spread = nltk.FreqDist(words_selected)
# spread.plot(50,cumulative=True)
spread_words = []
for word, frequency in spread.most_common(100):
  spread_words.append(word)
  # print(u'{};{}'.format(word, frequency))

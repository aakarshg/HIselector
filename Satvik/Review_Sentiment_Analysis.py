import pandas as pd
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

lemmatizer = WordNetLemmatizer()
stemmer = SnowballStemmer(language="english")

positive = ['good', 'great', 'awesome', 'cool', 'happy', 'amazing', 'satisfied', 'excellent', 'like', 'love', 'decent',
            'satisfactory', 'happiest']
negative = ['terrible', 'horrible', 'bad', 'worst', 'worse', 'illegal', 'lie', 'sucks', 'worthless', 'suck', 'upset',
            'poor', 'unhappy', 'dishonest', 'fail', 'denied', 'worse', 'beware', 'ridiculous', 'unacceptable', 'rude',
            'unfair', 'disappointed', 'useless', 'complaint', 'excuses', 'nightmare']
high_cost = ['costly', 'expensive', 'pricey', 'bankrupt', 'escalate']
low_cost = ['affordable', 'cheap']

pos_count = 0
neg_count = 0
high_cost = 0
low_cost = 0



for each in negative:
    print(lemmatizer.lemmatize(each))
    print(stemmer.stem(each))
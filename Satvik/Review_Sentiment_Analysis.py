import pandas as pd
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
import ast

lemmatizer = WordNetLemmatizer()
stemmer = SnowballStemmer(language="english")

reviews = pd.read_csv(".\\Reviews.csv", encoding="latin")
reviews['Reviews'] = reviews['Reviews'].apply(lambda x: ast.literal_eval(x))

positive = ['good', 'great', 'awesome', 'cool', 'happy', 'amazing', 'satisfied', 'excellent', 'like', 'love', 'decent',
            'satisfactory', 'happiest']
negative = ['terrible', 'horrible', 'bad', 'worst', 'worse', 'illegal', 'lie', 'sucks', 'worthless', 'suck', 'upset',
            'poor', 'unhappy', 'dishonest', 'fail', 'denied', 'worse', 'beware', 'ridiculous', 'unacceptable', 'rude',
            'unfair', 'disappointed', 'useless', 'complaint', 'excuses', 'not', 'nightmare', 'avoid', 'greed']
high_cost = ['costly', 'expensive', 'pricey', 'bankrupt', 'escalate', 'higher']
low_cost = ['affordable', 'cheap']

positive = [stemmer.stem(w) for w in positive]
negative = [stemmer.stem(w) for w in negative]
high_cost = [stemmer.stem(w) for w in high_cost]
low_cost = [stemmer.stem(w) for w in low_cost]

pos_list = []
neg_list = []
high_list = []
low_list = []

for each in reviews['Reviews']:
    pos_count = 0
    neg_count = 0
    high_count = 0
    low_count = 0
    num_reviews = len(each)
    if num_reviews != 0:
        review_overall = ' '.join(each)
        words = word_tokenize(review_overall)
        words = [w.lower() for w in words if w.isalpha()]
        stop_words = set(stopwords.words('english'))
        words_clean = [w for w in words if w not in stop_words]
        stemmed_words = [stemmer.stem(w) for w in words_clean]
        for word in stemmed_words:
            if word in positive:
                pos_count += 1
            if word in negative:
                neg_count += 1
            if word in high_cost:
                high_count += 1
            if word in low_cost:
                low_count += 1
    pos_list.append(pos_count)
    neg_list.append(neg_count)
    high_list.append(high_count)
    low_list.append(low_count)

reviews['Pos_Count'] = pos_list
reviews['Neg_Count'] = neg_list
reviews['High_Count'] = high_list
reviews['Low_Count'] = low_list

reviews.to_csv("C:\\Users\\satvi\\Documents\\DDDM\\Project\\Review_Table.csv", index=False)
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import operator
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


def dump_keys(d, lvl=0):
    for k, v in d.items():
        print('%s%s' % (lvl * ' ', k) + " -- " + str(v))
        if type(v) == dict:
            dump_keys(v, lvl+1)


tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')

intake = open('/home/jesse/DDDM/HIselector/data/Health_Insurance_plans.TXT').read()

words = word_tokenize(intake)

vectorizer = TfidfVectorizer(min_df=1)

X = vectorizer.fit_transform(words)

idf = vectorizer.idf_

my_dict = dict(zip(vectorizer.get_feature_names(), idf))
my_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))

dump_keys(my_dict )

#print(intake)
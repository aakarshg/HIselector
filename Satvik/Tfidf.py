from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
intake = open('.\\Bag of Words\\doc1.txt').read()
words = word_tokenize(intake)
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(words)
idf = vectorizer.idf_
print (dict(zip(vectorizer.get_feature_names(), idf)))


vectorizer = TfidfVectorizer(min_df=0.0009, stop_words='english', smooth_idf=True,
                     norm="l2", sublinear_tf=False, use_idf=True, ngram_range=(1, 3), analyzer='word')
intake1 = open('.\\Bag of Words\\relevant_sentences.txt').read()
words1 = word_tokenize(intake1)
#vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(words1)
idf = vectorizer.idf_
diction = dict(zip(vectorizer.get_feature_names(), idf))
print(len(diction))
print (sorted(diction.items(), key= lambda x: x[1] , reverse=True))

#print(intake)
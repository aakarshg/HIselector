from textblob import TextBlob
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from PyDictionary import PyDictionary
from inflection import singularize
import io

dictionary = PyDictionary()
data = io.open('class.TXT', encoding ='UTF-8').read()
bunch = TextBlob(data)
find_good = bunch.sentences

political_list = ['campaigning','government','civics','election','legislature',\
                 'statecraft','Republican','people','national','government',\
                 'Obama','Clinton','Democrat','Senate','Minister','President',\
                 'reform','congress','federal']

state_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin',
'Wyoming']

inc_dec_list = ['decreasing', 'decrease', 'decreased', 'decline', 'declined', 'declining', 'dropping', 'drop', 'dropped', 'rise', 'rising', 'rose',
'increase', 'increasing', 'increased']

buckets = {}

buckets['political'] = political_list
buckets['states'] = state_list
buckets['inc_dec'] = inc_dec_list

sentence_list = []
for sentence in find_good:
    sentence.strip()
    count = 0
    for category in buckets:
        if(any(map(lambda word: word in sentence, buckets[category]))):
            count += 1
            continue
    if count == 2:
        sentence_list.append(str(sentence))

data = '\n'.join(sentence_list)
print sentence_list

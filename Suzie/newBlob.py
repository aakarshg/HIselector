from textblob import TextBlob
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from PyDictionary import PyDictionary
from inflection import singularize

dictionary = PyDictionary()
data = open('/Users/susannamoneta/Documents/NCSU/SrSm1/CSC495/Project1/test.txt').read()
bunch = TextBlob(data)

find_good = bunch.sentences

technical_list = open("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\Jesse\\technical_key_words.txt").read().split("\n")
technical_extension = ['health', 'insurance', 'federal', 'care']
for word in technical_extension:
	technical_list.extend( word )

legal_list = ['law', 'legal', 'regulation', 'effective', 'order', 'lawful', 'valid', 'judicial', 'court', 'rule', 'system', 'control', 'government', 'governor', 'councilman']

state_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin',
'Wyoming']

inc_dec_list = ['decreasing', 'decrease', 'decreased', 'decline', 'declined', 'declining', 'dropping', 'drop', 'dropped', 'rise', 'rising', 'rose',
'increase', 'increasing', 'increased']

buckets = {}

for word in ['legal', 'law', 'system', 'governor']:
    legal_list.extend(dictionary.synonym(word))
for word in ['technical', 'technology']:
    technical_list.extend(dictionary.synonym(word))
for word in ['increase', 'incline', 'decrease', 'decline']:
	inc_dec_list.extend(dictionary.synonym(word))

word = list(set(legal_list))
technical_list = list(set(technical_list))

buckets['legal'] = legal_list
buckets['technical'] = technical_list
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

words = word_tokenize(data)

# Pre-cleaning
spread = FreqDist(words)
spread.plot(50)
for word,freq in spread.most_common(100):
    print(u'{};{}'.format(word, freq))

# Cleaning
words = [w.lower().singularize() for w in words if w.isalpha()]
stop_words = set(stopwords.words('english'))
words_clean = [w for w in words if w not in stop_words]

# Post-Cleaning
spread = FreqDist(words_clean)
spread.plot(50)
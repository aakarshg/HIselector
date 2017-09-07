from textblob import TextBlob
from PyDictionary import PyDictionary
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# dictionary = PyDictionary("economic","legal","technical","ethical","political")
dictionary = PyDictionary()

data = open("C:\\Users\\satvi\\Documents\\DDDM\\Classwork\\Bag of Words\\Company_Profiles_and_Directories_US_Law_Revi2017-08-24_13-46.txt", encoding='utf-8').read()

bunch = TextBlob(data)
find_good = bunch.sentences

# good_word_dict_1 = {}
# for d in dictionary.getSynonyms():
#     good_word_dict_1.update(d)

good_word_dict_2 = {}
ethical_list = open("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\Satvik\\Bag of Words\\Ethical_words.txt").read().split("\n")
technical_list = open("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\Jesse\\technical_key_words.txt").read().split("\n")
for word in ['ethical', 'ethics', 'ethic']:
    ethical_list.extend(dictionary.synonym(word))
for word in ['technical', 'technology']:
    technical_list.extend(dictionary.synonym(word))
ethical_list = list(set(ethical_list))
technical_list = list(set(technical_list))

good_word_dict_2['ethical'] = ethical_list
good_word_dict_2['technical'] = technical_list

sentence_list = []
for sentence in find_good:
    sentence.strip()
    count = 0
    for category in good_word_dict_2:
        if(any(map(lambda word: word in sentence, good_word_dict_2[category]))):
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
words = [w.lower() for w in words if w.isalpha()]
stop_words = set(stopwords.words('english'))
words_clean = [w for w in words if w not in stop_words]

# Post-Cleaning
spread = FreqDist(words_clean)
spread.plot(50)

f=open("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\Satvik\\Bag of Words\\relevant_sentences.txt","w", encoding='utf-8')
f.write(data)
f.close()
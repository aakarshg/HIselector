from freq_analysis import data 
from textblob import TextBlob

bunch = TextBlob(data)
words = TextBlob(open( '/home/jesse/DDDM/HIselector/Jesse/technical_key_words.txt', encoding='UTF-8' ).read()).words

all_sentences = bunch.sentences

# good_words = spread_words
# good_words = ['health', 'service', 'plan', 'consumer', 'caregiver', 'plans',
#         'coinsurance', 'income', 'copayment', 'applicable', 'associated',
#         'developmental', 'deductibles', 'requirements', 'liability', 'disabilities']

invalidChars = ['?', ')', '(', ',', ':', '\'', '-', '*', '.' ]

for sentence in all_sentences:

    if( any(map(lambda word: word in sentence, words))):
        print(sentence + "\n\n")
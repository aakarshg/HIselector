from freq_analysis import *
from textblob import TextBlob

bunch = TextBlob(data)

all_sentences = bunch.sentences

# good_words = spread_words
good_words = ['health', 'service', 'plan', 'consumer', 'caregiver', 'plans',
        'coinsurance', 'income', 'copayment', 'applicable', 'associated',
        'developmental', 'deductibles', 'requirements', 'liability', 'disabilities']

invalidChars = ['?', ')', '(', ',', ':', '\'', '-', '*', '.' ]

for sentence in all_sentences:

    if( any(map(lambda word: word in sentence, good_words))):
        print(sentence + "\n\n")

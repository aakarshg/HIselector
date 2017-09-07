from textblob import TextBlob
data = open('/Users/susannamoneta/Documents/NCSU/SrSm1/CSC495/Project1/test.txt').read()
bunch = TextBlob(data)

find_good = bunch.sentences

key_words = ['law', 'Law', 'legal', 'Legal', 'health', 'Health', 'insurance', 'Insurance', 'federal', 'Fedearal', 'Care', 'care', 'Alabama', 'Alaska',
'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin',
'Wyoming', 'decreasing', 'decrease', 'decreased', 'decline', 'declined', 'declining', 'dropping', 'drop', 'dropped', 'rise', 'rising', 'rose',
'increase', 'increasing', 'increased']

for sentence in find_good:
	if(any(map(lambda word: word in sentence, key_words))):
		print(sentence)
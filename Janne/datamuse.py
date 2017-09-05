''' 
  This class will handle all interactions with the datamuse api
'''

import requests

MAIN_URL = "https://api.datamuse.com/words?"

GET_RELATED_WORDS = "ml="

def get_related_words_for(word):
  request = MAIN_URL + GET_RELATED_WORDS + word
  response = datamuse_request(request)
  
  related_words = []
  if response not None:
    for word_info in response:
       related_words.append(word_info["word"])

  return related_words

def datamuse_request(request):
  return requests.get(request).json()


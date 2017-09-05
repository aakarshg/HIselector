# -------------------------------------------------------------------- #
# This class will handle all interactions with the datamuse api        #
# Documentation for the datamuse.api can be found at:                  #
# https://www.datamuse.com/api/                                        #
# -------------------------------------------------------------------- #

import requests

MAIN_URL = "https://api.datamuse.com/words?"

GET_RELATED_WORDS = "ml="

def get_related_words_for(word):
  request = MAIN_URL + GET_RELATED_WORDS + word
  response = datamuse_request(request)
  
  related_words = []
  if response:
    # Get list of related words
    for word_info in response:
       related_words.append(word_info["word"])

    # add the main word into the list
    related_words.append(word)

  return related_words

def datamuse_request(request):
  return requests.get(request).json()


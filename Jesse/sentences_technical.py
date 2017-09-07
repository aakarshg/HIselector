# -------------------------------------------------------------------- #
# This program will take a text file as an input and output any        #
# sentences containing any words that match a certain criteria.        #
# The sentences printed out provide more context and specificity       #
# for the gathering data from the input file.                          #
#                                                                      #
# Created by: JLA 9/5/2017, modified by Jesse Simpson                  #
# -------------------------------------------------------------------- #

import argparse

import datamuse_technical
from textblob import TextBlob

def get_args():
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('--data_source', type=str, help='file to process')
  return parser.parse_args()

def main():
  # args = get_args()

  # data_source = args.data_source
  data_source = '/home/jesse/DDDM/Data.txt'

  # Get words from file
  word_file = open( '/home/jesse/DDDM/HIselector/Jesse/technical_key_words.txt', encoding='UTF-8' ).read()
  useful_words = TextBlob(word_file)
  useful_word_list = useful_words.words

  # Create buckets
  word_buckets = {}
  for word in useful_word_list:
    word_buckets[word] = None

  for bucket_header in word_buckets:
    word_buckets[bucket_header] = datamuse_technical.get_related_words_for(bucket_header)

  # Parse data for sentences containing related words
  with open(data_source, encoding="utf-8") as data:
    bunch = TextBlob(data.read())
    sentences = bunch.sentences
    
    for sentence in sentences:
      sentence.strip()
      if sentence:
        # Check all word buckets
        contains_key_word = False
        for bucket in word_buckets:
          if (any(map(lambda word: word in sentence, word_buckets[bucket]))):
            contains_key_word = True

        if contains_key_word:
          print (sentence + '\n') 

if __name__ == "__main__":
  main()
    

'''
  This sen+ences class will positively select sentences that contain
  keywords from the specified words bucket list.
'''

import argparse

import datamuse
from textblob import TextBlob

def get_args():
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('--data_source', type=str, help='file to process')
  return parser.parse_args()

def main():
  args = get_args()

  data_source = args.data_source

  # Create buckets
  # word_buckets = {'cost': None, 'increase': None, 'decrease': None}
  word_buckets = {'increase': None}
  for bucket_header in word_buckets:
    word_buckets[bucket_header] = datamuse.get_related_words_for(bucket_header)

  # Parse data for sentences containing related words
  with open(data_source, encoding="utf-8") as data:
    bunch = TextBlob(data.read())
    sentences = bunch.sentences
    
    for sentence in sentences:
      # Check all word buckets
      for bucket in word_buckets:
        if (any(map(lambda word: word in sentence, word_buckets[bucket]))):
          print (sentence) 

if __name__ == "__main__":
  main()
    

# -------------------------------------------------------------------- #
# This program will take a text file as an input and output any        #
# sentences containing any words that match a certain criteria.        #
# The sentences printed out provide more context and specificity       #
# for the gathering data from the input file.                          #
#                                                                      #
# Created by: JLA 9/5/2017                                             #
# -------------------------------------------------------------------- #

import argparse
import os
import datamuse
from textblob import TextBlob


def get_args():
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('--data_source', type=str, help='file to process')
  return parser.parse_args()

def getRelatedWordsForBucket( bucketType ): 
  for bucket_header in bucketType:
    bucketType[bucket_header] = datamuse.get_related_words_for( bucket_header );
  return bucketType



# parses data for sentences containing related words.
# data_source is the file location for the data
# bucketType is the particular bucket whether it is economic or procedural or etc.
# output file location is the path to the output file.
def parseDataForSentencesContainingRelatedWords(data_source, bucketType, output_file_location):
  f = open(output_file_location,'w')
  with open(data_source, encoding="utf-8") as data:
    bunch = TextBlob(data.read())
    sentences = bunch.sentences
    
    for sentence in sentences:
      sentence.strip()
      if sentence:
        # Check all word buckets
        contains_key_word = False
        for bucket in bucketType:
          if (any(map(lambda word: word in sentence, bucketType[bucket]))):
            contains_key_word = True

        if contains_key_word:
          f.write( str(sentence) + '\n')
  f.close()


# main program
def main():
  args = get_args()

  data_source = args.data_source

  # Create buckets
  economic_word_buckets = {'cost': None, 'increase': None, 'decrease': None}
  political_word_buckets = {'campaigning': None,'government': None,'civics': None,'election': None,'legislature': None,
                 'statecraft': None,'Republican': None,'people': None,'national': None,'government': None,
                 'Obama': None,'Clinton': None,'Democrat': None,'Senate': None,'Minister': None,'President': None,
                 'reform': None,'congress': None,'federal': None}

  ethical_list = open("Satvik/Bag of Words/Ethical_words.txt").read().split("\n")
  technical_list = open("data/technical_key_words.txt").read().split("\n")
  ethical_word_buckets = {}
  technical_word_buckets = {}
  for item in ethical_list:
    ethical_word_buckets[item] = None
  for item in technical_list:
    technical_word_buckets[item] = None
    
  
  economic_word_buckets = getRelatedWordsForBucket(economic_word_buckets)
  ethical_word_buckets = getRelatedWordsForBucket(ethical_word_buckets)
  technical_word_buckets = getRelatedWordsForBucket(technical_word_buckets)


  # Parse data for sentences containing related words
  parseDataForSentencesContainingRelatedWords(os.path.join("data", "health-insurance-AND-cost.TXT"), economic_word_buckets, 
  os.path.join("output", "economicSentences.TXT"))

  # parseDataForSentencesContainingRelatedWords(os.path.join("[politics-sentences]"), ethical_word_buckets, 
  # os.path.join("output", "ethicalSentences.TXT"))

  parseDataForSentencesContainingRelatedWords(os.path.join("data", "Health_Insurance_plans.TXT"), technical_word_buckets, 
  os.path.join("output","technicalSentences.TXT"))

if __name__ == "__main__":
  main()
    

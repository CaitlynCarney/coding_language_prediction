import time
import os
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd
import json
from bs4 import BeautifulSoup
import requests
import unicodedata
import re

from env import github_token, github_username
#-----------------------------------------------------------------------------

def drop_nulls(dw):
    '''Takes null values from dataframe
    drops all the nulls'''
    # drop all the nulls
    dw.dropna(inplace=True)
    # return df
    return dw

#-----------------------------------------------------------------------------

def basic_clean(string):
    '''Takes in string
    makes everything lowercase
    removes incosistent text
    only keeps anything a-z, 0-9, ' and white space'''
    # make everything lowercase
    string = string.lower()
    # removes incosistencies in the text
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    # set what to keep
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    # return new cleaned string
    return string

def tokenize(string):
    '''Takes in the string provided by basic_clean funciton
    creates a tokenizer
    uses the tokenizerr on the cleaned string'''
    # Create the tokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()
    # Use the tokenizer
    string = tokenizer.tokenize(string, return_str = True)
    # return tokenized string
    return string

def stem(string):
    '''In string from the basic_clean and tokenize fucntion
    creaters the porter stemmer
    applies the porter stemmer to every word in the string provided
    joing the list of words back into a string'''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    # Apply the stemmer to each word in our string
    stems = [ps.stem(word) for word in string.split()]
    # Join the list of words into the string
    string_stemmed = ' '.join(stems)
    # return string_stemmed
    return string_stemmed

def lemmatize(string):
    '''Takes in string from basic_clean and tokenize funcitons
    creates a lematizer
    uses the lematizer on each word in the string
    merges the list of words back into string format
    and returns the now lematized string'''
    # Create the Lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    # Use the lemmatizer on each word using split
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    # Join the list into a string
    string_lemmatized = ' '.join(lemmas)
    # return lemmatized string
    return string_lemmatized

def remove_stopwords(string, exclude_words=[], extra_words=[]):
    '''takes in string from basic clean and tokenize fucntions
    takes in a list of words to exclude from the stopword list
    take sin a list of words to include in the stopword list
    makes the list of stopwords
    removes words listed from stopword list
    add words listed to stopword list
    remove words from stopword list from the string
    join words back to string format
    return new string'''
    # set stopword list 
    stopword_list = stopwords.words('english')
    # remove exclude_words list from stopword list
    stopword_list = set(stopword_list) - set(exclude_words)
    # add extra_wrods list to stopword list
    stopword_list = stopword_list.union(set(extra_words))
    # remove stopword list words from string
    string = string.split()
    # set filtered words value
    filtered_words = [word for word in string if word not in stopword_list]
    # join words back into string format 
    string = ' '.join(filtered_words)
    # return new string
    return string
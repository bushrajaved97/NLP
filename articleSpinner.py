# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:32:05 2019

@author: bushr
"""

import nltk 
import random 
import numpy as np
from builtins import range
import bs4 as bs 
import urllib.request 

source = urllib.request.urlopen('https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/nlp_class/electronics/positive.review').read()
soup = bs.BeautifulSoup(source,'lxml')
text = ""
for paragraph in soup.find_all('review_text'):
    text += paragraph.text

conversation = """

this is a beautiful day. i am very happy today. what about you ?
"""
# load the reviews
# data courtesy of http://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html

# extract trigrams and insert into dictionary
# (w1, w3) is the key, [ w2 ] are the values
trigrams = {}

s = text.lower()
tokens = nltk.tokenize.word_tokenize(s)
for i in range(len(tokens) - 2):
    k = (tokens[i], tokens[i+2])
    if k not in trigrams:
        trigrams[k] = []
    trigrams[k].append(tokens[i+1])

# turn each array of middle-words into a probability vector
trigram_probabilities = {}
for k, words in trigrams.items():
    # create a dictionary of word -> count
    if len(set(words)) > 1:
        # only do this when there are different possibilities for a middle word
        d = {}
        n = 0
        for w in words:
            if w not in d:
                d[w] = 0
            d[w] += 1
            n += 1
        for w, c in d.items():
            d[w] = float(c) / n
        trigram_probabilities[k] = d


def random_sample(d):
    # choose a random sample from dictionary where values are the probabilities
    r = random.random()
    cumulative = 0
    for w, p in d.items():
        cumulative += p
        if r < cumulative:
            return w

print("Original" , conversation)
tokens = nltk.tokenize.word_tokenize(conversation)
for i in range(len(tokens) - 2):
    if random.random() < 0.2: # 20% chance of replacement
        k = (tokens[i], tokens[i+2])
        if k in trigram_probabilities:
            w = random_sample(trigram_probabilities[k])
            tokens[i+1] = w
        
print("Spun:")
print(" ".join(tokens).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!"))


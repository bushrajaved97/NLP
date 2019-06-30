# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:49:26 2019

@author: bushr
"""

import nltk
import re
import heapq
import numpy as np
text="""Hello! What can I do for you? Good Morning Doctor. I am not well.Come and sit here. Open your mouth. How long are you not well? 
Since yesterday. No problem-did you have Motion yesterday? No Doctor-not so freely. Doctor I feel giddy. I don’t feel like eating at all. 
then? I feel like vomiting. Do you take a lot of water? 
No, doctor I don’ take too much. Did you take any medicine? Yes Doctor, I took Anacin. 
who told you to take it? Nobody Doctor I took it myself. why did you take it? Because I felt headache. Nothing to be worried at. 
Do you need immediate relief? No need sir. It is enough you give medicines. 
"""


#preprcessing the data
text=re.sub(r'\[[0-9]*\]',' ',text)
text=re.sub(r'\s+',' ',text)
clean_text=text.lower()
clean_text=re.sub(r'\W',' ',clean_text)
clean_text=re.sub(r'\d',' ',clean_text)
clean_text=re.sub(r'\s+',' ',clean_text)

#tokenizing paragraph into sentences
sentences=nltk.sent_tokenize(text)
stop_words=nltk.corpus.stopwords.words('english')

#buildng Histogram
word2count={}
for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word]=1
        else:
            word2count[word]+=1
            
freqwords = heapq.nlargest(100,word2count,key=word2count.get)

# IDF Matrix
word_idfs = {}

for word in freqwords:
    doc_count = 0
    for data in sentences:
        if word in nltk.word_tokenize(data):
            doc_count += 1
    word_idfs[word] = np.log((len(text)/doc_count)+1)

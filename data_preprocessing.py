import csv
import re
import numpy as np
import pandas as pd
import os
import nltk 
import string
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 
ps = nltk.PorterStemmer()

def cleanData(txt):
	# print(txt)
	txt = "".join([c for c in txt if c not in string.punctuation])
	# print(txt)
	tokens = re.split('\W+',txt)
	txt = [ps.stem(word) for word in tokens if word not in stop_words and word != '']
	return txt


filename = "annotations_metadata.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
    fields = next(csvreader) 
   
    for row in csvreader: 
        rows.append(row) 

n = len(rows)


direc = "all_files"

f = open("dataset_stemmed" + '.txt' , "w+", encoding='utf-8')

for file in os.listdir(direc):
    curr = open(direc +"/" + file, "r")
    line = curr.read()
    cleanTxt = cleanData(line)
    tagged = [u for u in nltk.pos_tag(cleanTxt) if u[1] != 'NNP']
    tokenised_with_POS = " ".join([''.join(u) for u in tagged])
    print(tokenised_with_POS)

    for i in range(0,n):
        if str(file) == str(rows[i][0])+".txt":
        	if(rows[i][4]=="noHate"):
        		tag = 0
        	else:
        	    tag = 1
        
        	f.write(str(tokenised_with_POS) + "	" + str(tag) + '\n')



     
        

  


   

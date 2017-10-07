import csv
import sys
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

'''
author : Abhijeet Singh
date : 06/08/2017 
'''

filename = "american.csv"

fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
     
    fields = next(csvreader)
 
    for row in csvreader:
        rows.append(row)

for row in rows:
    for col in row:
        print(row)
        print ("\n")
        # analysing tweets by tokenizing them
        analysis = TextBlob(col)
        print("\t",analysis.sentiment)
        print("\n")
        
import csv
import sys
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

filename = "dunkirk.csv"

fields = []
rows = []
count  = 0
count1 = 0
count2 = 0
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
     
    fields = next(csvreader)
 
    for row in csvreader:
        rows.append(row)

pol = 0
avg = 0
sub = 0 

for row in rows:
    for col in row:
        print(row)
        # analysing tweets by tokenizing them
        analysis = TextBlob(col)
        pol = analysis.sentiment.polarity
        sub = analysis.sentiment.subjectivity
        count1 += pol
        count2 += sub
        if pol < 0.5 :
            avg += 1
        count += 1
        print("\t",analysis.sentiment)
        print("")
        
print("")
print("Avg. Polarity : ", count1/count)
print("Avg. Subjectivity : ", count2/count)
print("The avg rating from the above data : ", (avg/count)*100)
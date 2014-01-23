import csv
from collections import Counter

# Create array for all neighborhoods in file
allNeighborhoodsArray = []

with open('transit-cuts-neighborhoods.txt','rb') as tsvin, open('new.csv', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvout = csv.writer(csvout)

    for row in tsvin:
        #print row[0]
        allNeighborhoodsArray.append(row[0])

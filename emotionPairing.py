"""
	determine the frequency of emotional pattern from sentence to sentence
	does happiness follow sadness, does interest follow anger
	most frequent emotions
	emotion used the MOST frequently
	emotion used LESS frequenty
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
	program takes csv file
	of tags and keeps
	a count of
	tag-pair frequency

	IE. [INTR -VALI] 50

"""



import sys
import csv
import re
import collections
from collections import Counter
from itertools import chain, combinations

headers = None
dataDict = []
file = 'tagsChat224moniceO.csv'
reader=csv.reader(open(file,'rU'))

for row in reader:
	dataDict.append(row)
    #dataDict[row[0]]['Stabling'] = [s.strip() for s in dataDict[row[0]]['Stabling'].split(',')]


frequencyOfEmotion = Counter(chain.from_iterable(combinations(row, 1) for row in dataDict))
print frequencyOfEmotion


pairs = [[x,y] for (x, y) in zip(dataDict[:-1], dataDict[1:])]

print pairs[1]
print pairs[2]

pairsTally = {}
i = 0

writer = csv.writer(open('pairCountChat224moniceO.csv', 'wb'))
for row in pairs:
	print row
	print pairs.count(row)
   	writer.writerow([row, pairs.count(row)])


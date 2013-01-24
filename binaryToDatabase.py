"""
    Created by: Karen C. Aragon
    Senior Research Project

    binaryToDatabase.py

    Description: put sentencesWithBinary.csv into binaryDb

"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import csv

con = None

try:

    con = mdb.connect('localhost', 'root', 
        'rachoes123', 'postsData');

    cur = con.cursor()

    binary_Data = csv.reader(file('binary.csv'))

    """
     CREATE TABLE   sentencesWithBinary(sentenceID INT(11), 
                    PRIMARY KEY(sentenceID), 
                    paragraphInPost INT(11), 
                    sentenceInParagraph INT(11), 
                    speaker VARCHAR(11), 
                    annotator_1 INT(11), annotator_2 INT(11), annotator_3 INT(11), 
                    annotator_4 INT(11), annotator_5 INT(11), annotator_6 INT(11), annotator_7 INT(11), annotator_8 INT(11), 
                    annotator_9 INT(11), annotator_10 INT(11), annotator_11 INT(11), annotator_12 INT(11))
    """

    # sentenceID, paragraphInPost, sentenceInParagraph speaker
    cur.execute('INSERT INTO sentencesWithBinary (sentenceID, paragraphInPost, sentenceInParagraph, speaker)')
    cur.execute("SELECT sentenceID, paragraphInPost, sentenceInParagraph, speaker FROM sentences ORDER BY sentenceID ASC")

    # import binary data into sentencesWithBinary table
    for row in binary_Dat:
        print row
        cur.execute('INSERT INTO sentencesWithBinary (annotator_1,annotator_2, annotator_3, annotator_4, annotator_5, annotator_6, annotator_7, annotator_8, annotator_9, annotator_10, annotator_11, annotator_12) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
           
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1]) 
    sys.exit(1)
    
finally:    
    if con:    
        con.close()
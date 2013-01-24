"""
    Created by: Karen C. Aragon
    Senior Research Project

    Description: script coverts emotion sentences_tags
        into binary values and puts 24bit binary encodin
        into the postsData database


"""



#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import csv

con = None

sentenceAnnotDict = {}
binaryAnnotDict = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}

tagNamesDict = {1:"INTR",2:"VALI",3:"AFFE",4:"GRAT",5:"PEAC" ,
                6:"EXJD" ,7:"PRID" ,8:"HUMR" ,9:"THMR" ,10:"TENS" ,
                11:"FEAR" ,12:"SADN" ,13:"FRST" ,14:"ANG" ,15:"CONT" ,
                16:"DOMI" ,17:"BELL", 18:"DEFN", 19:"DISG" ,20:"STON" ,
                21:"WHIN" ,22:"SHME" ,23:"GILT" ,24:"EMBR"}
try:

    con = mdb.connect('localhost', 'root', 
        'rachoes123', 'postsData');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    data = cur.fetchone()
    print "Database version : %s " % data

    cur.execute("SELECT sentenceID, tagID, annotatorID FROM sentences_tags ORDER BY sentenceID ASC")
    rows = cur.fetchall()

    #get number of rows
    numrows = int(cur.rowcount)
    print 'Number of rows: ' + str(numrows) + '\n'

    """
        for each sentence replace annotatorID's tags with binary value

        UPDATE values
         cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", 
        ("Guy de Maupasant", "4"))        
    
        print "Number of rows updated: %d" % cur.rowcount
    """
    for annotator in binaryAnnotDict:
        binaryAnnotDict[annotator] = '00000000000000000000000'
    emotion = None
    binaryValue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    i = 0
    for row in rows[0:192]:
        sentenceID = row[0]
        if row[0] == sentenceID:
            for key in tagNamesDict:
                if row[1] in tagNamesDict:
                    binaryValue[row[1]] = 1
                    binaryAnnotDict[row[2]] = ''.join(map(str, binaryValue))
                    sentenceAnnotDict[row[0]] = binaryAnnotDict.items() 
            binaryValue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        else:
            for key in tagNamesDict:
                if row[1] in tagNamesDict:
                    binaryValue[row[1]] = 1
                    binaryAnnotDict[row[2]] = ''.join(map(str, binaryValue))
                    sentenceAnnotDict[row[0]] = binaryAnnotDict.items()
            binaryValue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    print sorted(sentenceAnnotDict.items())

    writer = csv.writer(open('binary.csv', 'wb'))
    for key, value in sentenceAnnotDict.items():
        writer.writerow([key, value])
   
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
    if con:    
        con.close()
"""
    Created by: Karen C. Aragon
    Senior Research Project

"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import csv

con = None

try:

    con = mdb.connect('localhost','root', 'rachoes123','postsData');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    data = cur.fetchone()
    print "Database version : %s " % data

    csv_data = csv.reader(file('binary.csv'))
    cur.execute('load data local infile binary.csv into table percent fields terminated by ',' (sentenceID, annotator_1 , annotator_2 , annotator_3 , annotator_4 , annotator_5 , annotator_6 , annotator_7 , annotator_8 , annotator_9 , annotator_10 , annotator_11 , annotator_12 )')
    con.commit()
    

except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
    if con:    
        con.close()
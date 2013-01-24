"""
    Created by: Karen C. Aragon
    Senior Research Project

    Description: parses speaker from db

"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import csv
import re

con = None

try:
    con = mdb.connect('localhost', 'root', 
        'rachoes123', 'postsData');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    data = cur.fetchone()
    print "Database version : %s " % data
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

    cur.execute(sql)

    #print sorted(sentences)


except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
    if con:    
        con.close()


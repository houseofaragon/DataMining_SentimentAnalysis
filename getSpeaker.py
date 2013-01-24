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
    con = mdb.connect('localhost','root', 'rachoes123','postsData');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    data = cur.fetchone()
    print "Database version : %s " % data

    cur.execute("SELECT sentenceID, sentence, paragraphInPost FROM sentences WHERE sentenceInParagraph = 1")
    sentences = cur.fetchall()


    #print sorted(sentences)

   # sentence[0] = sentenceID
   # sentence[1] = sentence
   # sentence[2] = paragraphInPost

    speaker =''
    sentencesList = []
    for sentence in sentences:
        if sentence[1][0] =='[':
            #[Oct 26, 2011 4:55:59 PM PDT] wendy k 
            #[Oct 26, 2011 4:55:59 PM PDT] ketly
            speaker = re.search(r'(])+(\s\w*\s?\w*\s*)',sentence[1])
            #print str(sentence0]) + speaker.group(2)
            cur.execute("INSERT INTO parseSpeakers(sentenceID,speaker,paragraphInPost)  VALUES ('%d','%s','%d' % (sentence[0], speaker.group(2), sentence[2]))")

        elif sentence[1][0] == '(':
            #(02:53:13 PM) cheryl has entered the chat.  
            speaker= re.search(r'(\))+(\s\w*\s)',sentence[1])
            print str(sentence0]) + + speaker.group(2)
            #cur.execute("INSERT INTO parseSpeakers(sentenceID,speaker, paragraphInPost)  VALUES ('%d','%s','%d" % (sentence0], speaker.group(2), sentence[2]))

        elif sentence[1].find('(') == -1:
            speaker = sentence[1]
            #print str(sentence0])  + + speaker
            cur.execute("INSERT INTO parseSpeakers(sentenceID,speaker,paragraphInPost)  VALUES ('%d','%s','%d' % (sentence[0], speaker, sentence[2]))")
        
        elif sentence[1][0].isalpha() or sentence[1][:-1] == ')':
            #Debbie3 (04:45:42 PM) 
            #speaker = sentence[1]
            speaker= re.search(r'(\w*\s)+(\()',sentence[1])
            #print str(sentence0])  + + speaker.group(1)
            cur.execute("INSERT INTO parseSpeakers(sentenceID,speaker,paragraphInPost)  VALUES ('%d','%s','%d' % (sentence[0], speaker.group(1), sentence[2])")

        con.commit()

	writer = csv.writer(open('binary.csv', 'wb'))
    	for key, value in sentenceAnnotDict.items():
        	writer.writerow([key, value])

except mdb.Error, e:
    print "Error %d: %s" % (e.args0],e.args[1])
    sys.exit(1)
    
finally:    
    if con:    
        con.close()

"""
[Oct 26, 2011 4:55:59 PM PDT] wendy k 
[Oct 26, 2011 4:55:59 PM PDT] ketlyne  
speaker= re.search(r'(])+(\s\w*\s?\w*\s*)',s)


[Oct 26, 2011 4:55:59 PM PDT] wendy k joined.
# need to search if string ends in a period and remove last word

(02:53:13 PM) cheryl has entered the chat.  
speaker= re.search(r'(\))+(\s\w*\s)',s)

Debbie3 (04:45:42 PM) 
speaker= re.search(r'(\w*\s)+(\()',s)

if sentence[row]0] ==[':
    #[Oct 26, 2011 4:55:59 PM PDT] wendy k 
    #[Oct 26, 2011 4:55:59 PM PDT] ketly
    speaker= re.search(r'(])+(\s\w*\s?\w*\s*)',s)

else if sentence[row]0] ==(':
    #(02:53:13 PM) cheryl has entered the chat.  
    speaker= re.search(r'(\))+(\s\w*\s)',s)

else:
    #Debbie3 (04:45:42 PM) 
    speaker= re.search(r'(\w*\s)+(\()',s)

|     166498 |               4 | [Oct 26, 2011 4:54:43 PM PDT] ketlyne joined.                       |
|     166499 |               5 | [Oct 26, 2011 4:55:56 PM PDT] amandag joined.                       |
|     166500 |               6 | [Oct 26, 2011 4:55:59 PM PDT] ketlyne                               |
|     166503 |               7 | [Oct 26, 2011 4:56:44 PM PDT] amandag         
|     166640 |              58 | [Oct 26, 2011 5:48:53 PM PDT] gr82balive left.                      |
|     166641 |              59 | [Oct 26, 2011 5:48:55 PM PDT] gr82balive joined.  

|     531722 |               1 | (02:53:13 PM) cheryl has entered the chat.                          |
|     531723 |               2 | (02:53:19 PM) Jose has entered the chat.                            |
|     531724 |               3 | cheryl (02:53:33 PM)                                                |
|     531726 |               4 | Jose (02:53:44 PM)    

|     224474 |               9 | (04:43:33 PM) Debbie3 has entered the chat.                         |
|     224475 |              10 | (04:43:39 PM) Jocelyn has entered the chat.    
|     224494 |              20 | Debbie3 (04:45:42 PM)    

Hello, I have a database that stores the sentences of different blog posts. I am currently 
trying to use Python regex to loop through the sentences and parse out just the name.
The problem is they are different formats.



if sentence[row]0] ==[':
    #[Oct 26, 2011 4:55:59 PM PDT] wendy k 
    #[Oct 26, 2011 4:55:59 PM PDT] ketly
    speaker= re.search(r'(])+(\s\w*\s?\w*\s*)',s)

else if sentence[row]0] ==(':
    #(02:53:13 PM) cheryl has entered the chat.  
    speaker= re.search(r'(\))+(\s\w*\s)',s)

else:
    #Debbie3 (04:45:42 PM) 
    speaker= re.search(r'(\w*\s)+(\()',s

"""

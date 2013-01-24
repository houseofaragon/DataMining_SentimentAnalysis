#!/usr/bin/python
# -*- coding: utf-8 -*-



d = {111:{1:[1,1,1], 2:[1,0,1], 3:[0,0,0]},
	  222:{1:[0,1,1], 2:[0,0,1], 3:[1,1,0]}}

for key,values in d.iteritems():
	for x in range(3):
		print values[1]

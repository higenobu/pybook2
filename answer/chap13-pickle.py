#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
import sys
import csv


wks=[]
lk=[]
datafile='cardealer.csv'
	
ff=open(datafile,'r')
conts=ff.readline()
while (conts):
				
	print (conts)
	conts=conts.strip()
	cc=conts.split(',')
	print (cc)

	lk.append((cc[0],cc[1],cc[2],cc[3],cc[4],cc[5],cc[6],cc[7]))
	conts=ff.readline()
ff.close()
print (lk)

              
print ("pickle file")
ll=pickle.dumps(lk)
	   
with open('pickleb.txt','wb') as pp:
	pp.write(ll)
with open('pickleb.txt','rb') as rr:
	pk=rr.read()	
	wpk=pickle.loads(pk)
	print (wpk)
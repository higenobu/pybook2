#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
import sys
import csv
if __name__ == '__main__':

	wks=[]
	lk=[]
	datafile='cardealer.csv'
	wfile='car2022.csv'

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

	
	
	with open(wfile,'w') as ww:
		for i in range(len(lk)):
			print (lk[i])
			ww.write(lk[i][0]+','+lk[i][1]+','+lk[i][2]+','+lk[i][3]+','+lk[i][4]+','+lk[i][5]+','+lk[i][6]+','+lk[i][7]+'\n')
              

	print ("pickle file")
	ll=pickle.dumps(lk)
	list_again=pickle.loads(ll)
	#print (list_again)    
	with open('pickleb.txt','wb') as pp:
		pp.write(ll)
	with open('pickleb.txt','rb') as rr:
		pk=rr.read()	
		wpk=pickle.loads(pk)
		print (wpk)
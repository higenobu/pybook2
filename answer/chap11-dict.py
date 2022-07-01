#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
import sys
import csv
if __name__ == '__main__':

	wks=[]
	lk=[]
	datafile='jmdict.txt'
	wfile='dictej.txt'
	begin=0
	wj=''
	j=0
	
	
	ff=open(datafile,'r',encoding='utf-8')
	conts=ff.readline()
	while (conts ):
		j+=1		
		#print (conts)
		conts=conts.strip()
	
		if (conts[0:4]=='<ent'):
			wj=wj+conts
			begin=1
			conts=ff.readline()
		elif (conts[0:4]=='</en'):
			begin=0
			wj=wj+conts
			#print (wj)
			lk.append(wj)
			wj=''
			conts=ff.readline()
		elif (begin==1):
			wj=wj+conts
			conts=ff.readline()
		else:
			conts=ff.readline()


		
		
	ff.close()
	print (len(lk))
	dicno=0
	jdic=[]
	edic=[]
	for i in range(len(lk)):
		cont=lk[i]
		cc=cont.split('<')
		for k in range(len(cc)):
			dd=cc[k].split('>')
			#print (dd)
			if (dd[0]=='keb'):
				print ("J:",dd[1])
				dicno+=1
				jdic.append([dicno,dd[1]])
			elif (dd[0]=='gloss'):
				print ("E:",dd[1])
				edic.append([dicno,dd[1]])
		
	#print (jdic)
	#print (edic)
	jdicno=dict()
	edicno=dict()
	ejdict=dict()
	diclist=[]
	for j in range(len(jdic)):
		dicno=jdic[j][0]
		dicv=jdic[j][1]
		jdicno[dicno]=dicv
		edicno[edic[j][0]]=edic[j][1]
	#print (jdicno)	
	#print (edicno)
	print (len(edicno))
	for i in range(1,len(edicno)):
		if (i in edicno):
			ejdict[edicno[i]]=jdicno[i]
			diclist.append([edicno[i],jdicno[i]])
	print (ejdict)
	
	
	with open(wfile,'w',encoding='utf-8') as ww:
		for i in range(len(diclist)):
			print (diclist[i])			
			ww.write(diclist[i][0]+','+diclist[i][1]+'\n')
			

	
	print ("pickle file")
	ll=pickle.dumps(ejdict)
	#ll2=pickle.loads(ll)
	#print (list_again)    
	with open('pickle-ejdic.txt','wb') as pp:
		pp.write(ll)
	'''
	with open('pickleb-ejdic.txt','rb') as rr:
		pk=rr.read()	
		wpk=pickle.loads(pk)
		print (wpk)
	'''
import sys
import csv


diffs=[]
datafile='nikkei-data.csv'
lk=[]
with open(datafile,'r') as ff:
	reader=csv.reader(ff,delimiter=',')
	for row in reader:
		lk.append(row)
for dd in range(50):
		# assume: date:0,end-price:1, start-price:2
	diff=float(lk[dd][1])-float(lk[dd][2])
	jdate=lk[dd][0]
	print (diff)
	diffs.append([jdate,diff])
print (diffs)

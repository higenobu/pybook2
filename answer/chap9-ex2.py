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
		#high:3,low:4
	diff=abs(float(lk[dd][3])-float(lk[dd][4]))
	jdate=lk[dd][0]
	print (diff)
	diffs.append([jdate,diff])
print (diffs)	
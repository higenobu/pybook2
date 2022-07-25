import sys
import csv
if __name__ == '__main__':

	diffs=[]
	datafile='nikkei-data.csv'
	with open(datafile,'r') as ff:
		reader=csv.reader(ff,delimiter=',')
		lk=[row for row in reader]
	

	for dd in range(50):
		#high:3,low:4
		diff=abs(float(lk[dd][3])-float(lk[dd][4]))
		jdate=lk[dd][0]
		print (diff)
		diffs.append([jdate,diff])
	print (diffs)	

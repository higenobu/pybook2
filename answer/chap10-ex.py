import sys
import csv

wks=[]
lk=[]
datafile='work07.csv'
wfile='calc07.csv'
with open(datafile,'r') as ff:
	reader=csv.reader(ff,delimiter=',')
	for row in reader:
		lk.append(row)
	
	
print (lk)
for dd in range(len(lk)):
	wka=str(float(lk[dd][1])*float(lk[dd][4]))
	wkb=str(float(lk[dd][2])*float(lk[dd][5]))
	wkc=str(float(lk[dd][3])*float(lk[dd][6]))
	jdate=lk[dd][0]
		
	wks.append([jdate,wka,wkb,wkc])

print (wks)	

with open(wfile,'w') as ww:
	for i in range(len(wks)):
		ww.write(wks[i][0]+','+wks[i][1]+','+wks[i][2]+','+wks[i][3]+'\n')
              
          
import sys
import csv
if __name__ == '__main__':

	data=''
	datafile='nikkei_stock_average_daily_jp.csv'
	with open(datafile,'r') as ff:
		reader=csv.reader(ff,delimiter=',')
		lk=[row for row in reader]
	for dd in range(50):
		data=data+','+str(lk[dd][1])
	print (data)
	

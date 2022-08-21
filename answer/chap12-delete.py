import sys
import pickle
if __name__ == '__main__':

	
	wfile='dictej.txt'
	addfile='new-ejdict.txt'
	efile='english.txt'
	wej=dict()
	yobi=dict()
	
	ff=open(wfile,'r',encoding='utf-8')
	conts=ff.readline() 
	while (conts): 
		con=conts.strip()
		cc=con.split(',')
		wd=cc[0].split(' ')
		for j in range(len(wd)):
			swd=wd[j].strip('()')

			if swd in wej:
				pass
			else:
				wej[swd]=cc[1]
				print (swd,wej[swd])
		wej[cc[0]]=cc[1]
		conts=ff.readline()
	ff.close()
	#**************************************************
	with open(addfile,'w',encoding='utf-8') as ww:
		for wd in wej.keys():
			print (wd)			
			ww.write(wd+','+wej[wd]+'\n')
	
	

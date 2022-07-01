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
	
	'''
	ee=open(efile,'r')
	econt=ee.readline() 
	sent=''
	while (econt):
		
		econt=econt.strip()
		cc=econt.split(' ')
		#print (cc)
		for i in range(len(cc)):
			
			if (cc[i] in wej):
				jword=wej[cc[i]]
			elif (cc[i] in yobi):
				jword=yobi[cc[i]]
			else:
				jword=cc[i]
			sent=sent+' '+jword+' '
		print (sent)
		econt=ee.readline()
	ee.close()
	'''
	'''	
	ww=input("english:")
	ww.strip()
	print (wej[ww])
	
	with open('pickle-ejdic.txt','rb') as rr:
		pk=rr.read()	
		wpk=pickle.loads(pk)
		#print (wpk)
	ww=input("english:")
	ww.strip()
	print (wpk[ww])
	'''
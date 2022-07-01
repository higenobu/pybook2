import sys
import pickle
if __name__ == '__main__':

	'''
	wfile='dictej.txt'
	
	wej=dict()
	ff=open(wfile,'r',encoding='utf-8')
	conts=ff.readline() 
	while (conts):
		#print (conts) 
		con=conts.strip()
		cc=con.split(',')
		wej[cc[0]]=cc[1]
		conts=ff.readline()
	ff.close()
	
	ww=input("english:")
	ww.strip()
	print (wej[ww])
	'''
	with open('pickle-ejdic.txt','rb') as rr:
		pk=rr.read()	
		wpk=pickle.loads(pk)
		#print (wpk)
	ww=input("english:")
	ww.strip()
	print (wpk[ww])
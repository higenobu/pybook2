import sys

if __name__ == '__main__':

	
	
	addfile='new-ejdict.txt'
	efile='english.txt'
	jfile='japanese.txt'
	wej=dict()
	
	#sample dictionary temporaly created 
	#please make your own dictionary



	ff=open(addfile,'r',encoding='utf-8')
	conts=ff.readline() 
	while (conts): 
		con=conts.strip()
		cc=con.split(',')	
		wej[cc[0]]=cc[1]		
		conts=ff.readline()
	ff.close()
	#output file
	gg=open(jfile,'w',encoding='utf-8')
	#input english sentences	
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
			
			else:
				jword=cc[i]
			sent=sent+' '+jword+' '
		print (sent)
		gg.write(sent+'\n')
		econt=ee.readline()
	ee.close()
	gg.close()
	
	


def select_wdpt(h,p):
	
	words=''
	

	for k in range(len(h)):
		if (k>=p):
			if (h[k]=='　'):
				r=[words,k]
				break
			else:
				words=words+h[k]			
				k+=1
	else:
		r=[words,k]
	return r


renga = '満月や　ボトル枕に　ホームレス　野ざらしを　心に風の　しむ身かな'


ff=open('haiku.csv','r')
h=ff.readline()
j=0
while (h and j<3):


	h=h.strip()
	print (h)
	h=ff.readline()
	
	p=0
	n=0
	k=0
	while (p<=len(h)):
		if (n % 3 == 0):
			k=0
		elif (n %3 == 1):
			k=1
		else:
			k=2
		kup=select_wdpt(h,p)
		print ("ku"+str(k)+':',kup[0])
		p=kup[1]+1
		n+=1
	j+=1	



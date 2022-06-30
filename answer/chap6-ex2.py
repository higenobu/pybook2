
def select_wdpt(h,p):
	
	words=''
	
	if (len(h)<=0):
		r=['',0]
		return
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



kami=[]
naka=[]
shimo=[]
kamifile='kami.csv'
nakafile='naka.csv'
shimofile='shimo.csv'
kup=[]

ff=open('haiku.csv','r')
h=ff.readline()
j=0
while (h):


	h=h.strip()
	print (h)
	
	
	p=0
	n=0
	k=0
	while (p<=len(h)):
		
		kup=select_wdpt(h,p)
		if (kup[0]==''):
			p+=1
			continue
		
		if (n % 3 == 0):
			k=0
			kami.append(kup[0])
		elif (n %3 == 1):
			k=1
			naka.append(kup[0])
		else:
			k=2	
			shimo.append(kup[0])	
		print ("ku"+str(k)+':',kup[0])
		p=kup[1]+1
		n+=1
	j+=1
	h=ff.readline()

with open(kamifile,'w') as ww:
	for km in kami:
		km=km.strip()
		ww.write(km+'\n')
with open(nakafile,'w') as ww:
	for nk in naka:
		nk=nk.strip()
		ww.write(nk+'\n')
with open(shimofile,'w') as ww:
	for sh in shimo:
		sh=sh.strip()
		ww.write(sh+'\n')

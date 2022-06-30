


kami=[]
naka=[]
shimo=[]
ffile='first.txt'
sfile='second.txt'
mfile='merge.txt'
kup=[]

ff=open(ffile,'r')
gg=open(sfile,'r')
h=ff.readline()
g=gg.readline()
ih=0
ig=0
maxint=999999

while (h or g):
	
	if (h):
		h=h.strip()
		print ("First:",h)
		ih=int(h)
	else:
		ih=maxint
		print ('fend',h,ih)
		
	if (g):
		g=g.strip()
		print ("Second",g)	
		ig=int(g)
	else:
		ig=maxint
		print ('gend',g,ig)
		

	if (ih>ig):
		kup.append(g)
		g=gg.readline()
	elif (ih<ig):
		kup.append(h)
		h=ff.readline()
	elif (ih==maxint and ig==maxint):
		print (ih,ig)
		break
	else:
		kup.append(h)
		g=gg.readline()
		h=ff.readline()
with open(mfile,'w') as ww:
	for sh in kup:		
		ww.write(sh+'\n')

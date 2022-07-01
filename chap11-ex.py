

import csv
kami=[]
naka=[]
shimo=[]
ffile='ejdict-hand-utf8.txt'
sfile='second.txt'
mfile='merge.txt'
lk=[]
kup=[]

with open(ffile,'r') as ff:
	reader=csv.reader(ff,delimiter=',')
	lk=[row for row in reader]
'''
ff=open(ffile,'r')
gg=open(sfile,'r')
h=ff.readline()
g=gg.readline()


while (h):
	
	if (h):
		h=h.strip()
		print ("First:",h)

		kup.append(h)
		
		h=ff.readline()
with open(mfile,'w') as ww:
	for sh in kup:		
		ww.write(sh+'\n')
'''
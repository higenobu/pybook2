import math

kfile='kakaku.csv'
addk=0
kup=[]

ff=open(kfile,'r')
h=ff.readline()
j=0
while (h):


	h=h.strip()
	addk=addk+int(h)
	kup.append(int(h))
	j+=1
	
	
	h=ff.readline()
#print (addk)
print ("no:",j)
avgk=int(addk/j)
print ("average:",avgk)
print ("max and min:",max(kup),min(kup))
addw=0
for i in range(len(kup)):
	wh=(kup[i]-avgk)**2
	addw=addw+wh
sqrt_addw=math.sqrt(addw)
hensa=sqrt_addw/j
print ("hensa",hensa)

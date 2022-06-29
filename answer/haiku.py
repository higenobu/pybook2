
def select_part(h):
	
	k=0
	print ('word length:',h,len(h))
	for k in range(len(h)):
		if (h[k]=='　'):
			r=k
			break
		else:			
			k+=1
	else:
		r=k	
	return r


haiku = '満月や　ボトル枕に　ホームレス'

p=0
kamip=select_part(haiku)
print ("kami",kamip,haiku[0:kamip])
nakap=select_part(haiku[kamip+1:])
print ("naka",nakap,haiku[kamip+1:kamip+1+nakap])
shimop=select_part(haiku[kamip+1+nakap+1:])
print ("shimo",shimop,haiku[kamip+1+nakap+1:])


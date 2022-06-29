
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


#haiku = '満月や　ボトル枕に　ホームレス'
allhaiku='初しぐれ　猿も小蓑を　ほしげなり/\
しぐるるや　黒木つむ屋の　窓あかり/\
こがらしや　頬腫れ痛む　人の顔/\
鳥どもも　寝入っているか　余呉の海/\
下京や　雪つむ上の　夜の雨'


hh=allhaiku.split('/')
#print (hh)
for k in range(len(hh)):
	hk=hh[k]
	bubun=hk.split('　')
	print (bubun)

haiku=hh[0]
p=0
kamip=select_part(haiku)
print ("kami",kamip,haiku[0:kamip])
nakap=select_part(haiku[kamip+1:])
print ("naka",nakap,haiku[kamip+1:kamip+1+nakap])
shimop=select_part(haiku[kamip+1+nakap+1:])
print ("shimo",shimop,haiku[kamip+1+nakap+1:])


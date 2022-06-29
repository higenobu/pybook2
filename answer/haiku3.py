
def select_pt(h,p):
	
	words=''
	print ('word length:',h,len(h))

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


haiku = '満月や　ボトル枕に　ホームレス'
#haiku = '満月や ボトル枕に ホームレス'
#haiku = '満月やA　ボトル枕にB　ホームレス'

p=0
kamip=select_pt(haiku,p)
print ("kamiku",kamip[0])

nakap=select_pt(haiku,kamip[1]+1)
print ("naka7",nakap[0])
shimop=select_pt(haiku,nakap[1]+1)
print ("shimoku",shimop[0])


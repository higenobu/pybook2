
def select_pt(h,p):
	
	
	print ('word length:',h,len(h))

	for k in range(len(h)):
		if (k>=p):
			if (h[k]=='　'):
				r=k
				break
			else:			
				k+=1
	else:
		r=k	
	return r


haiku = '満月や　ボトル枕に　ホームレス'
#haiku = '満月や ボトル枕に ホームレス'
#haiku = '満月やA　ボトル枕にB　ホームレス'

p=0
kamip=select_pt(haiku,p)
print ("kamiku",kamip,haiku[0:kamip])

nakap=select_pt(haiku,kamip+1)
print ("naka7",nakap,haiku[kamip+1:nakap])
shimop=select_pt(haiku,nakap+1)
print ("shimoku",shimop,haiku[nakap+1:])


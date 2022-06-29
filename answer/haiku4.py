
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


renga = '満月や　ボトル枕に　ホームレス　野ざらしを　心に風の　しむ身かな'

#haiku = '満月や ボトル枕に ホームレス'
#haiku = '満月やA　ボトル枕にB　ホームレス'

p=0

while (p<=len(renga)):
	kup=select_pt(renga,p)
	print ("ku",kup[0])
	p=kup[1]+1




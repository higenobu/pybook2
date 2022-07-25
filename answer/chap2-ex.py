def substr(data,s,l):
	if (len(data)>=l):
		result=data[s:l]
	else:
		result=data[s:]
	return result

print ('晴れ')
print('京都旅行/銀閣寺にちかくにおいしそうな蕎麦屋に入ってみた。')
print ('京都名物のにしんそばを頼むと手打ちそばで驚いた')
bun='京都旅行/銀閣寺にちかくにおいしそうな蕎麦屋に入ってみた。'
first=substr(bun,0,4)
print (first)
second=substr(bun,5,100)
print (second)
bun2='京都名物のにしんそばを頼むと手打ちそばで驚いた'
bubun=substr(bun2,5,10)
print (bubun)

#!/usr/bin/env python

katakana= u"ーァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"

hiragana = u"ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ" 
zenspace='　'
'''
file=open('2.txt','r')
word=''
mm=file.read()
#memo=mm.decode('utf-8')

for m in mm:
    if m in katakana:
    	word=word+m
    else:
        print (word)
        word=''
file.close()


file=open('1.txt')
word=''
mm=file.read()
#memo=mm.decode('utf-8')
for m in mm:
    if m in hiragana:
    	word=word+m
    else:
        print (word)
        word=''
file.close()
'''

file=open('haiku.txt')
word=''
mm=file.read()

for m in mm:
    if not (m in hiragana or m in katakana or m in zenspace):
    	word=word+','+m
    else:
        print (word)
        
file.close()
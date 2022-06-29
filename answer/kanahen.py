#!/usr/bin/env python

katakana= u"ーァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"

hiragana = u"ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ" 

file=open('2.txt','r')
word=''
mm=file.read()
for m in mm:
    if m in katakana:
    	word=word+m
    else:
        print (word)
        word=''
file.close()


file=open('2.txt')
word=''
mm=file.read()
for m in mm:
    if m in hiragana:
    	word=word+m
    else:
        print (word)
        word=''
file.close()
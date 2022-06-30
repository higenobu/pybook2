#!/usr/bin/env python

katakana= u"ーァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"

hiragana = u"ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ" 
zenspace='　\n'


wdc=[]
for j in range(1000):
    wdc.append(0)
    

wd=[]
def find_kanji(w):
    for i in range(len(wd)):
        if (wd[i]==w):
            rval=i 
            wdc[i]=wdc[i]+1
            break
    else:
        print ('no word',w)
        wd.append(w)
        rval=len(wd)
        print (rval)
        wdc[rval]=1
        
        
    return rval


def add_hindo(w):
    i=find_kanji(w)
    
    

file=open('haiku.txt')


mm=file.read()


for m in mm:
    if not (m in hiragana or m in katakana or m in zenspace):
    	add_hindo(m)
    
print (wd)
for k in range(len(wd)):
    print (wd[k],wdc[k])
    

       
file.close()
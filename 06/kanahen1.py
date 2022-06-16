#カタカナとひらがな，それぞれを全部使って文字列を作成し代入．
#最初にuを付けて，Unicode形式であることを宣言．
katakana = u'ーァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ'

hiragana = u'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ'

file = open('1.txt') #ファイルを開く
word = ''  #変数（word）を空に設定
mm = file.read()  #ファイルの中味を全部読み込んでmmに代入

#文字がカタカナであるかどうかの判定
for m in mm:
  if m in katakana:
    word = word + m  #カタカナであればwordに付加
  else:
    print(word)  #カタカナでなければwordを出力し，空に設定
    word=''
file.close()

#以下は，文字がひらがなであるかの判定，および文字列の抽出
file = open('1.txt')
mm = file.read()
for m in mm:
  if m in hiragana:
    word = word + m
  else:
    print(word)
    word = ''
file.close()

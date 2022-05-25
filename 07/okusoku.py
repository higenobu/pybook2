from random import randint
def okusoku():
    num = randint(1,100)
    print('1から100のどの数字が出るか予測してください')
    gs = input('予測した数字を入力します')
    gi = int(gs)
    while gi:
           if num == gi:
               print('当たりです',gi)
               break
           elif num > gi:
               print('もっと大きいです')
           else:
               print('もっと小さいです')
           gi = int(input('次の予測は？'))
okusoku()

import turtle

#関数のコード
def takakkei(kame,nagasa,kaku):
  angle = 360 / kaku
  for k in range(kaku):
    kame.fd(nagasa)
    kame.rt(angle)

#描画作成のコード
kame = turtle.Turtle()
print(kame)
takakkei(kame,50,10)
turtle.mainloop()

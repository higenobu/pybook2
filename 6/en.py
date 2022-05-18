import turtle
import math

def takakkei(kame,nagasa,kaku):
  angle = 360/kaku
  for k in range(kaku):
    kame.fd(nagasa)
    kame.rt(angle)

def en(kame,r):
  ensyu = 2 * math.pi * r
  n = 100
  nagasa = ensyu / n	
  takakkei(kame,nagasa,n)

kame = turtle.Turtle()
en(kame,50)
turtle.mainloop()

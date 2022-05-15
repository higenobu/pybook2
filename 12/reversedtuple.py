t = (4,3,5,8,2)
ww = tuple()
r = reversed(t)
for k in r:
  ww = ww[0:]+(k,)
print(ww)

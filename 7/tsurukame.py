def tsurukame(head,leg):
  x = 0
  y = 0
  while x <= head:
    y = head - x
    if (x * 2 + y * 4) == leg:	
      print('亀の数は',x)
      print('鶴の数は',y)
      break
    x += 1
  else:
    print('答えがありません') 
tsurukame(10,24)

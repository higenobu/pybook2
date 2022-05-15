import time
file = open('happy.txt')
kurikaeshi = 1
memo = file.readline()
while kurikaeshi <20:
  print(memo)
  time.sleep(1)
  kurikaeshi += 1
  memo = file.readline()
file.close()

import time
file = open('happy.txt')
memo = file.readline()
while len(memo) > 0:
  print(memo)
  time.sleep(1)
  memo = file.readline()
file.close()

import time
file = open('happy.txt')
for kurikaeshi in range(1,20):
  memo = file.readline()
  print(memo)
  time.sleep(1)
file.close()

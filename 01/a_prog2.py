file = open('data.txt') 
num = 0
total = 0 
data = file.readline() 
while (data):
  print (data) 
  num = num + 1 
  total = total + data 
  data = file.readline()
heikin = total / num 
file.close()
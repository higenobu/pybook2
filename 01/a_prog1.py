file = open('data.txt')
while (data):
  data = file.readline() 
  print(data) 
  num = num + 1
  total = total + data 
heikin = total / num 
file.close()

read_file = open('file.txt','r')
for ln in read_file:
  ln = ln.strip()
  print(ln)
read_file.close()

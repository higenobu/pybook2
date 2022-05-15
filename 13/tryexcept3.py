try:
  ff = open('sample_file.txt','w')
  for zaiko in zaikos:
    ff.write(str(zaiko) + '\n')
  print ('正しく書き込みました')
except:
  print ('エラーがおきました')
finally:
  ff.close()

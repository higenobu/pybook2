import pickle
data = (4,3,5,8,2)
pickle_data = pickle.dumps(data)
with open('binaryfile.txt','w') as ff:
  wdata = ff.write(str(pickle_data))

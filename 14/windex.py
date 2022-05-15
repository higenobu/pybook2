class Windex:
  def __getitem__(self,suji):
    return suji*3
a=Windex()
for ii in range(10):
  print (a[ii])

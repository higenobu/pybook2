class Wsample:
  def __getitem__(self,ii):
    return self.data[ii]
b = Wsample()
b.data = 'abcd'
for ww in b:
    print(ww)

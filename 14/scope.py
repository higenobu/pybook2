class  Scope:
  data='abcdefg'
  def __init__(self,value):
    self.value = value
  def display(self):
    data='hijklmn'
    print (self.data,data,self.value,Scope.data)
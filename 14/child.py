class Human:
  def setname(self,name):
    self.name = name
  def display(self):
    print(self.name)

class Student(Human):
  def school(self,schoolname):
    self.schoolname = schoolname
  def display(self):
    print(self.name,self.schoolname)

class Child(Student):
  def __init__(self,name):
    self.name=name
  def __eq__(self,other):
    if(self.schoolname==other.schoolname): return True
    else: return False 

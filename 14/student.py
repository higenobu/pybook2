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

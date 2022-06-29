#!/usr/bin/env python
import sys
import csv
import pickle
class Employee(object):

	def __init__(self,ssn,fname,lname,bod,address,tel,sal):
		self.ssn=ssn
		self.fname=fname
		self.lname=lname
		self.bod=bod
		self.address=address
		self.tel=tel
		self.sal=sal
		
		



	


	def add_sal(self,up):
		self.sal=int(self.sal)+int(up)
'''
	def  __repr__(self):

		return repr("ssn=%s,fname=%s,lname=%s,bod=%s,address=%s,tel=%s,sal=%s" % (self.ssn,self.fname,self.lname,self._bod,self._address,self._tel,self.sal))
'''
#emp=Employee(ssn='999-999-1111',fname='akira',lname='matsuo',bod='2000-01-01',address='aaaaa',tel='999-999-9999')
#print (emp)

class Staff(Employee):
	def __init__(self,ssn,fname,lname,bod,address,tel,sal,kubun):
		super().__init__(ssn=ssn,fname=fname,lname=lname,bod=bod,address=address,tel=tel,sal=sal)
		self.kubun=kubun


			
	def  __repr__(self):

		return repr("ssn=%s,fname=%s,lname=%s,bod=%s,address=%s,tel=%s,kubun=%s,sal=%d" % (self.ssn,self.fname,self.lname,self.bod,self.address,self.tel,self.kubun,self.sal))
class Manager(Employee):
	def __init__(self,ssn,fname,lname,bod,address,tel,sal,kubun):
		super().__init__(ssn=ssn,fname=fname,lname=lname,bod=bod,address=address,tel=tel,sal=sal)
		self.manager_level=manager_level


			
	def  __repr__(self):

		return repr("ssn=%s,fname=%s,lname=%s,bod=%s,address=%s,tel=%s,kubun=%s,sal=%d,manager_level=%s" % (self.ssn,self.fname,self.lname,self.bod,self.address,self.tel,self.kubun,self.sal,self.manager_level))




def update_staff_sal(emplist,wssn,up_sal):
	ii=0
	wemp=emplist[ii]
	print (wemp)
	print ("find this ssn:",wssn)
	while (wemp and ii<10):
		

	
		print ("ssn?",wemp.ssn)
		if (wemp.ssn==wssn):
			print ("exists",wemp)
			wemp.add_sal(up_sal)
			print ("new staff data",wemp)
			break
		ii+=1
		wemp=emplist[ii]

	else:
		print ("no such ssn and no update")
	
def load_emp(filename):
	global emplist
	with open(filename,'rb') as inf:
		emplist=pickle.load(inf)


menu=input('menu:')
#0->add
#1->update

emplist=[]
filename='ch15-file'
load_emp(filename)
print (emplist)
if (menu=='1'):
	print ("update salary")	
	wssn=input("find ssn:")
	wup=input("salary up?:")
	up_sal=int(wup)
	update_staff_sal(emplist,wssn,up_sal)
	print ("updated:",emplist)
	


else:
	print ("add more staff")


	add_staff=input("how many add staff:")
	
	for ii in range(int(add_staff)):
		ssn=input("ssn:")
		fname=input("fname:")
		lname=input("lname:")
		bod=input("bod:")
		address=input("address:")
		tel=input("tel:")
		kubun=input("kubun:")
		sal=input("sal:")

		wst=Staff(ssn=ssn,fname=fname,lname=lname,bod=bod,address=address,tel=tel,kubun=kubun,sal=sal)
	#wst.add_sal(int(up))
	
		print (wst)
		emplist.append(wst)
#print (emplist)



filename='ch15-file'
with open(filename,'wb') as outf:
	pickle.dump(emplist,outf)


filename='ch15-file'
load_emp(filename)
print ("emplist",emplist)




for ii in range(len(emplist)):
	wemp=emplist[ii]	
	print (ii,wemp.ssn,wemp.lname,wemp.fname,wemp.sal)
	

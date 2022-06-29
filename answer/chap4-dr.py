
xx=input("Python Clinicにようこそ!")
print (xx+" 様,ありがとうございます")
taion=input("熱はいかがでしょうか？")
mm=input("脈拍はいくらでしょうか？")
bb=input("血圧はいくらでしょうか？")
cc=input("症状は？")
print ("熱は"+taion+" 脈拍は"+mm+" 血圧は"+bb+" 症状は"+cc)

status=''
syoho=''
kensa=''

if (float(taion)<float(37)):
	status='Normal'
elif (float(taion)<float(38)):
	if (cc=='None'):
		status='Normal'
	else:
	 	status='kafunsyo'
elif (float(taion)>=float(38)):
	if (cc=='None'):
		status='Normal'
	
	elif (int(mm)>100):
		print ("Virus")
		syoho='tamifuru'
	else:
		print ('kaze')
		syoho='kazekusuri'
if (int(bb)>130):
	syoho='BPkusuri'
if (int(mm)>100):
	kensa='Hearttest'	 	

	
else:
	print ('残念ながらそれは扱っていません')

print (status+":"+syoho+":"+kensa)


import re
from datetime import datetime
import random
class Driver():   #driver class
	def __init__(self,fname,lname,vno,vmodel,num):
		self.fname=fname
		self.lname=lname
		self.vno=vno
		self.vmodel=vmodel
		self.num=num
	def print(self):
		return self.fname,self.lname,self.vno,self.vmodel,self.num

class Car(Driver):  #Driver subclass
	pass

c1=Car("Ramesh","Kumar","2345","Ertiga",9876534210)
c2=Car("Suresh","Yadav","7870","Swift",9878094210)
c3=Car("Lakshay","Bhateja","4567","Alto",8765429019)
c4=Car("Manish","Rao","6543","WagonR",876213456)
c5=Car("Naveen","Saini","5192","Swift Dzire",93251678902)
c6=Car("Praveen","Kumar","3467","Centro",57286194324)


list1=[]

list1.append(c1)
list1.append(c2)
list1.append(c3)
list1.append(c4)
list1.append(c5)
list1.append(c6)


class MiniCar(Driver):  #Driver subclass
	pass
	
mc1=MiniCar("Pawan","Kumar","1234","Nano",123434210)
mc2=MiniCar("Mohan","Lal","6791","Alto800",1456094210)
mc3=MiniCar("Vineet","Rao","4105","Maruti Suzuki",8765456119)
mc4=MiniCar("Om","Kapoor","7815","Zen",8765413456)
mc5=MiniCar("Vinay","Sharma","1254","WagonR",62579081389)
mc6=MiniCar("Shyam","Verma","2810","Eeco",42376970828)


list2=[]

list2.append(mc1)
list2.append(mc2)
list2.append(mc3)
list2.append(mc4)
list2.append(mc5)
list2.append(mc6)


class Auto(Driver):   #Driver subclass
	pass

a1=Auto("Akash","Sharma","9023","Auto",71763901230)
a2=Auto("Radha","Raman","5421","Auto",98780312424)
a3=Auto("Sachin","Panchal","1092","Auto",8765431442)
a4=Auto("Rajan","Kumar","1276","Auto",87623567889)
a5=Auto("Pawan","Shukla","3712","Auto",58170981268)
a6=Auto("Arun","Nandan","4217","Auto",31686901761)


list3=[]

list3.append(a1)
list3.append(a2)
list3.append(a3)
list3.append(a4)
list3.append(a5)
list3.append(a6)


class Bike(Driver):     #Driver subclass
	pass

b1=Bike("Jitendar","Grover","7895","Pulsar",5763901230)
b2=Bike("Randhir","Kumar","2176","CD Deluxe",435352424)
b3=Bike("Yashvant","Singh","4529","Bajaj CT",131431442)
b4=Bike("Rajesh","Jha","9016","Bullet",24243567889)
b5=Bike("Ravi","Qureshi","5410","Yamaha FZ",97604171278)
b6=Bike("Tarun","Chugh","6827","Apache",586970661659)


list4=[]

list4.append(b1)
list4.append(b2)
list4.append(b3)
list4.append(b4)
list4.append(b5)
list4.append(b6)


class User():   #User class
	def __init__(self,choice):
		self.choice=choice
		if self.choice=="1":
			self.fname=str(input("Enter your First Name : "))
			self.lname=str(input("Enter your Last Name : "))
			self.mob=str(input("Enter your Mobile Number : "))
			x=re.findall("[0-9]",self.mob)
			while(len(x)!=10):
				self.mob=str(input("WRONG INPUT!!\n Please enter valid mobile number : "))
				x=re.findall("[0-9]",self.mob)
			self.email=str(input("Enter your Email id : "))
			self.pickup=str(input("Enter your Pickup Location : "))
			list=['Haus Khas Village','Dwarka','Paschim Vihar','Ramjas College','Pitampura','Noida','Dharuhera','Downtown Bar','Rajwada','KLP College','Pushpanjali Hospital','Loco Shed Heritage','Iffco Chowk','Sadar Bazar','Sector 29','Fun n Food Village Road','Cyber City','Ambience Mall','MG Road Metro Station','Bristol Chowk','Gwal Pahari','Masjid','Sector 21','BPTP']
			self.drop=str(input("Enter your Drop Location : "))
			while(self.drop not in list):
				print("INVALID ENTRY!! \n Please enter valid place from the following list\n",list)
				self.drop=str(input("Enter your Drop Location : "))
			file=open(self.mob,'w')
			file.write("First Name : "+self.fname+"\n")
			file.write("Last Name : "+self.lname+"\n")
			file.write("Mobile No : "+self.mob+"\n")
			file.write("Email id : "+self.email+"\n")
			file.close()
			
		elif(self.choice=="2"):
			self.mob=str(input("Enter your mobile number : "))
			x=re.findall("[0-9]",self.mob)
			while(len(x)!=10):
				self.mob=str(input("WRONG INPUT!! \n Please enter valid mobile number : "))
				x=re.findall("[0-9]",self.mob)
			self.pickup=str(input("Enter your Pickup Location : "))
			self.drop=str(input("Enter your Drop Location : "))
			list=['Haus Khas Village','Dwarka','Paschim Vihar','Ramjas College','Pitampura','Noida','Dharuhera','Downtown Bar','Rajwada','KLP College','Pushpanjali Hospital','Loco Shed Heritage','Iffco Chowk','Sadar Bazar','Sector 29','Fun n Food Village Road','Cyber City','Ambience Mall','MG Road Metro Station','Bristol Chowk','Gwal Pahari','Masjid','Sector 21','BPTP']
			while(self.drop not in list):
				print("INVALID ENTRY!! \n Please enter valid place from the following list\n",list)
				self.drop=str(input("Enter your Drop Location : "))
			

def yes():
	mode=str(input("Enter the mode of payment\n 1.Cash\n2.Paytm(10%CashBack upto Rs.20 on first three rides)\n3.PhonePe(Get 50% cashback upto rs 50 on your first ride)\n4.Pay through UPI(Get your 1st ride free)\n"))
	if(mode=="1" or mode=="2" or mode=="3" or mode=="4"):
		print("!!ENJOY YOUR RIDE!!")
		expr=str(input("Enter your Experience for this ride : "))
		return mode
	else:
		print("Please Enter Valid Input: ")
		yes()

def no():
	reason=str(input("Give the reasons \n1.Personal Problem\n2.Driver Problem\n3.Price Problem\n4.Others\n"))
	if reason=="4":
		other=str(input("Enter your reason:  "))
	elif (reason!="1" and reason!="2" and reason!="3" and reason!="4"):
		print("Please Enter Valid Input: ")
		no()



def dist(drop):
	delhi=['Haus Khas Village','Dwarka','Paschim Vihar','Ramjas College','Pitampura','Noida']
	ddelhi=[26,13,25,33,36,43]
	rewari=['Dharuhera','Downtown Bar','Rajwada','KLP College','Pushpanjali Hospital','Loco Shed Heritage']
	drewari=[47,51,55,63,68,72]
	gurgaon=['Iffco Chowk','Sadar Bazar','Sector 29','Fun n Food Village Road','Cyber City','Ambience Mall']
	dgurgaon=[9,11,10,7,9,12]
	faridabad=['MG Road Metro Station','Bristol Chowk','Gwal Pahari','Masjid','Sector 21','BPTP']
	dfaridabad=[9,11,20,37,42,46]
	if(drop in delhi):
		return (ddelhi[delhi.index(drop)])
	elif(drop in rewari):
		return (drewari[rewari.index(drop)])
	elif(drop in gurgaon):
		return (dgurgaon[gurgaon.index(drop)])
	elif(drop in faridabad):
		return(dfaridabad[faridabad.index(drop)])




def vchoice(dist,vehicle):
	price=0
	if(dist<=15):
		if(vehicle=="1"):
			driver=random.choice(list1)
			price=dist*22
			print("Your Driver Details  are : \nDriver's Name : ",driver.fname,driver.lname,"\nVehicle No : ",driver.vno,"\nVehicle's Model : ",driver.vmodel,"\nDriver's Mobile No : ",driver.num)
			print("Your Price Is: " ,price)
			return price,driver
		elif(vehicle=="2"):
			driver=random.choice(list2)
			price=dist*18
			print("Your Driver Details  are : \nDriver's Name : ",driver.fname,driver.lname,"\nVehicle No : ",driver.vno,"\nVehicle's Model : ",driver.vmodel,"\nDriver's Mobile No : ",driver.num)
			print("Your Price Is: " ,price)
			return price,driver
		elif(vehicle=="3"):
			driver=random.choice(list3)
			price=dist*14
			print("Your Driver Details  are : \nDriver's Name : ",driver.fname,driver.lname,"\nVehicle No : ",driver.vno,"\nVehicle's Model : ",driver.vmodel,"\nDriver's Mobile No : ",driver.num)
			print("Your Price Is: " ,price)
			return price,driver
		elif(vehicle=="4"):
			driver=random.choice(list4)
			price=dist*12		
			print("Your Driver Details  are : \nDriver's Name : ",driver.fname,driver.lname,"\nVehicle No : ",driver.vno,"\nVehicle's Model : ",driver.vmodel,"\nDriver's Mobile No : ",driver.num)
			print("Your Price Is: " ,price)
			return price,driver
	
	else:	
		if(vehicle=="1"):
			driver=random.choice(list1)
			price=dist*26
			print("Your Driver Details  are : \nDriver's Name : ",driver.fname,driver.lname,"\nVehicle No : ",driver.vno,"\nVehicle's Model : ",driver.vmodel,"\nDriver's Mobile No : ",driver.num)
			print("Your Price Is: " ,price)
			return price,driver
		elif(vehicle=="2"):
			driver=random.choice(list2)
			price=dist*22
			print("Your Driver Details  are : \nDriver's Name : ",driver.fname,driver.lname,"\nVehicle No : ",driver.vno,"\nVehicle's Model : ",driver.vmodel,"\nDriver's Mobile No : ",driver.num)
			print("Your Price Is: " ,price)
			return price,driver
		elif(vehicle=="3"):
			driver=random.choice(list3)
			price=dist*18
			print("Your Driver Details  are : \nDriver's Name : ",driver.fname,driver.lname,"\nVehicle No : ",driver.vno,"\nVehicle's Model : ",driver.vmodel,"\nDriver's Mobile No : ",driver.num)	
			print("Your Price Is: " ,price)
			return price,driver
		elif(vehicle=="4"):
			driver=random.choice(list4)
			price=dist*16
			print("Your Driver Details  are : \nDriver's Name : ",driver.fname,driver.lname,"\nVehicle No : ",driver.vno,"\nVehicle's Model : ",driver.vmodel,"\nDriver's Mobile No : ",driver.num)
			print("Your Price Is: " ,price)
			return price,driver
	



choice=str(input("1.SIGN UP\n2.SIGN IN\n "))
while(choice!="1" and choice!="2"):
	choice=str(input("Please Enter valid input: \n"))
u=User(choice)
drop=u.drop
d=dist(drop)
vehicle=str(input("Enter your Vehicle choice:\n1.CAR \n2.MINI CAR \n3.AUTO \n4.BIKE\n"))
while(vehicle!="1" and vehicle!="2" and vehicle!="3" and vehicle!="4"):
	print("Please Enter Valid Choice : \n")
	vehicle=str(input("Enter your Vehicle choice:\n1.CAR \n2.MINI CAR \n3.AUTO \n4.BIKE\n"))
price,driver= vchoice(d,vehicle)
	
ride=str(input("Do you want to take this ride? : "))
if (ride=="Yes" or ride=="yes" or ride=="y"):
	file=open(u.mob,'a')
	file.write("\n\nUser Ride Details\n\n\n")
	file.write("Date: "+datetime.now().strftime("%d:%m:%Y"+"\n"))
	file.write("Time : "+datetime.now().strftime("%H:%M:%S"+"\n"))
	file.write("Pickup : "+u.pickup+"\n")
	file.write("Drop : "+u.drop+"\n")
	file.write("Price : "+str(price)+"\n")
	mode=yes()
	file.write("Mode of Payement :"+ str(mode)+"\n")
	file.write("Driver Details are : \n")
	file.write("First Name : "+driver.fname+"\n")
	file.write("Last Name : "+driver.lname+"\n")
	file.write("Driver's vehicle no : "+driver.vno+"\n")
	file.write("Vehicle model : "+driver.vmodel+"\n")
	file.write("Mobile no. : "+str(driver.num)+"\n")
	file.close()
elif (ride=="No" or ride=="no" or ride=="n"):
	no()

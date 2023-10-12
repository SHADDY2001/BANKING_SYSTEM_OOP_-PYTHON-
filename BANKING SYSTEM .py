# #PARENT CLASS : USER 
# HOLDS DETAILS OF USER
# HAS FUNCTION TO SHOW USER DETAIL 
# STORE DETAIL ABOUT ACCOUNT BALANCE 
# STORE DETAIL ABOUT AMOUNT 
# ALLO FOR DEPOSIT WITHDRAW VIEW BALANCE

class user():
	def __init__(self,name,age, gender):
		self.name = name
		self.age = age
		self.gender = gender


	def show_details(self):
			print("")
			print("Personal Details")
			print("")
			print("Name : ",self.name)
			print("Age : ",self.age)
			print("Gender : ",self.gender)


#CHILD CLASS
class bank(user):
	def __init__(self,name ,age ,gender):
		super().__init__(name,age,gender)
		self.balance = 0

	def deposit(self,amount):
	 self.amount = amount
	 self.balance = self.balance + self.amount	
	 print("ACCOUNT BALANCE HAS BEEN UPDATED : $",self.balance )

	def withdraw(self,amount):
	 self.amount = amount
	 if(self.amount > self.balance):
	 		print("INSUFFICIENT FUNDS")
	 else:
	 	self.balance = self.balance - self.amount
	 	print("ACCOUNT BALANCE HAS BEEN UPDATED : $",self.balance)

	
	def view_balance(self):
	 self.show_details()
	 print("ACCOUNT BALANCE HAS BEEN UPDATED : $",self.balance)


 

	 




johan = bank("Johan",28,"Male")
johan.deposit(350)
johan.withdraw(200)	
johan.view_balance()
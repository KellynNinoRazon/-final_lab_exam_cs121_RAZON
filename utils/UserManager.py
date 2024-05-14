from .User import *

class user_manager:
	user_accounts={}
	
	def load_users(self):
		pass
		

	def save_users():
		pass

	def validate_username(self,username):
		if username in self.user_accounts:
			self.validate_passwordvalidate_password(username)
		else:
			print("Username does not exist.")
			return
		
	def validate_password(self,username,password):
		password= input("Password: ")
		if self.user_accounts[username].password == password:
			return
		else:
			print("Wrong password")
		
	def register(self,username,password):
		username = input("Enter username: ")
		if username in self.user_accounts:
			print("Username already exists.")
			return
		else:
			password = input("Enter password: ")
			self.user_accounts[username] = {"Username":username, "Password":password, "Budget" : float(0),"Redeemable points":0,"Inventory":[]}
			print("Account created!")

	def login(self):
		username= input("Enter username: ")
		if self.validate_username(username)==True:
		    print("Logged in!")
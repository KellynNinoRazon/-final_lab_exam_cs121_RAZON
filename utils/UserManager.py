from .User import *
from .DiceGame import Dice_Game

class user_manager:
	def __init__(self,username,password):
		self.username=username
		self.password=password
		
	user_accounts={}
	
	def load_users(self):
		pass
		

	def save_users():
		pass

	def validate_username(self):
		if self.username in self.user_accounts:
			self.validate_password(self,self.username,self.password)
		else:
			print("Username does not exist.")
			input()
			return
		
	def validate_password(self,password):
		self.password= input("Password: ")
		if self.user_accounts[self.username].password == password:
			Dice_Game.menu()
		else:
			print("Wrong password")
		
	def register(self):
		username = input("Enter username: ")
		if username in self.user_accounts:
			print("Username already exists.")
			input()
			return
		else:
			password = input("Enter password: ")
			self.user_accounts[username] = {"Username":username, "Password":password, "Budget" : 0,"Redeemable points":0,"Inventory":[]}
			print("Account created!")

	def login(self):
		username= input("Enter username: ")
		if self.validate_username(username,self.password)==True:
		    print("Logged in!")
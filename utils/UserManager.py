import os
from .User import *
from .DiceGame import Dice_Game
dice_game=Dice_Game()
class user_manager:
		
	user_accounts={}
	
	def load_user(self):
		if not os.path.exists("Users.txt"):
			with open('Users.txt', 'w') as f:
				f.write("")
				
		else:
			with open("Users.txt", 'r') as f:
				for line in f:
					user = line.strip().split(',')
					self.user_accounts[user[0]] = Users(user[0], user[1])
					
	def save_users(self):
		with open('Users.txt', 'w') as f:
			for username, password in self.user_accounts.items():
				f.write(f'{username},{password.password}\n')

	def validate_username(self,username):
		if username in self.user_accounts:
			self.validate_password(username)
		else:
			print("Username does not exist.")
			input()
			return
		
	def validate_password(self,username):
		password= input("Password: ")
		if self.user_accounts[username].password == password:
			dice_game.menu(username)
		else:
			input("Wrong password\n")
		
	def register(self):
		username = input("Enter username(atleast 4 characters): ")
		if len(username)<4:
			input("Usernames must be atleast 4 characters,try again.\n")
			return
		else:
			if username in self.user_accounts:
				input("Username already exists.\n")
				return
			else:
				password = input("Enter password(atleast 8 characters): ")
				if len(password)<8:
					input("Password must be atleast 8 characters long,try again.\n")
					return
				else:
					self.user_accounts[username]=Users(username,password)
					print("Account created!\n")

	def login(self):
		username= input("Enter username: ")
		self.validate_username(username)
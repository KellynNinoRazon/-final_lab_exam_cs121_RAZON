from .User import*
from .Score import Scores
import random
import os
import datetime

class Dice_Game:
	scores={}

	def roll_dice():
		return random.randint(1,6)
			
	def load_scores(self):
		self.scores = {}
		if not os.path.exists("Scores.txt"):
			with open('Scores.txt', 'w') as f:
				f.write("")
		else:
			with open('Scores.txt', 'r') as f:
				for line in f:
					values = line.strip().split(',')
					username = values[0]
					score = int(values[1])
					win = int(values[2])
					Game_Id = values[3]
					if username not in self.scores:
						self.scores[username] = []
						self.scores[username].append(Scores(username,score,win, Game_Id))

	def save_scores(self):
		with open('Scores.txt', 'w') as f:
			for scores in self.scores.values():
				for Scores in scores:
					f.write(f"{Scores.username},{Scores.score},{Scores.win},{Scores.Game_Id}\n")
				
	def show_top_score(self):
		with open('Scores.txt', 'r') as f:
			lines = f.readlines()
			
			scores = []
			for line in lines:
				values = line.strip().split(',')
				username = values[0]
				score= int(values[1])
				win = int(values[2])
				Game_Id = values[3]
				scores.append(Scores(username, score, win, Game_Id))
				
			Scores.sort(key=lambda x: x[1], reverse=True)
			
			print("Top 10 Scores (Highest Wins):\n")
			for i, (username, score, win, Game_Id) in enumerate(scores[:10], start=1):
				print(f"{i}. Username: {username}, Wins: {win}, Score: {score}, GameID: {Game_Id}")

	def save_and_reset(self, username):
		Game_Id = datetime.datetime.now().strftime("%Y%m%d%H%M")
		if username in self.scores:
			self.scores[username].append(Scores(username, self.score, self.win, Game_Id))
		else:
			self.scores[username] = [Scores(username, self.score, self.win, Game_Id)]
			self.save_scores()
			self.score = 0
			self.win = 0

	def play_game(self,username):
		round_won=0
		stage_won=0
		while True:
			print(f"\nStarting game as {username}...")
			for i in range(3):
				player_rolled_dice=Dice_Game.roll_dice()
				print(f"{username} rolled: {player_rolled_dice}")
				cpu_rolled_dice=Dice_Game.roll_dice()
				print(f"CPU rolled: {cpu_rolled_dice}")
				if player_rolled_dice>cpu_rolled_dice:
					print(f"You win this round {username}!")
					round_won+=1
				elif player_rolled_dice==cpu_rolled_dice:
					print("It's a tie!")
				else:
					print("Cpu won this round!")
			print("---------------------")
			if round_won>=2:
				stage_won+=1
				round_won+=3
				self.scores[username]=Scores(username,round_won,stage_won,456890)
				print("You won this round!")
			else:
				print(f"You lost this stage {username}")

			choice1=Inputs(1,"Do you want to continue to the next stage?(1 for Yes,0 for No): ")
			if choice1==0:
				print(f"Total points:{round_won}, Total rounds won:{stage_won}")
				input("Thank you for playing.")
				return
			if choice1==1:
				continue
	def show_top_scores(self):
		with open('Scores.txt', 'r') as f:
			lines = f.readlines()
			
		scores = []
		for line in lines:
			values = line.strip().split(',')
			username = values[0]
			score = int(values[1])
			win = int(values[2])
			Game_Id = values[3]
			score.append((username, score, win, Game_Id))
			
		scores.sort(key=lambda x: x[1], reverse=True)
		
		print("Top 10 Scores (Highest Wins):\n")
		for i, (username, score, win, Game_Id) in enumerate(scores[:10], start=1):
			print(f"{i}. Username: {username}, Wins: {win}, Points: {score}, GameID: {Game_Id}")

	def logout(self):
		return
	
	def menu(self,username):
		while True:
			print(f"\nWelcome to the Dice Game {username}")
			print("1. Start Game\n2.Show top scores\n3.Exit")

			choice=Inputs(3,"Enter your choice, or leave blank to cancel:\n")
		
			if choice==1:
				Dice_Game.play_game(self,username)
			if choice==2:
				Dice_Game.show_top_scores(self)
			if choice==3:
				return
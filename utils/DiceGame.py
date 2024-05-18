from .User import *
from .Score import *
import random
import os
import datetime

class Dice_Game:
	scores={}
		
	score=0
	win=0

	def roll_dice():
		return random.randint(1,6)
	
	#Trying out diff codes
	'''def load_scores(self):
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
					f.write(f"{Scores.username},{Scores.score},{Scores.win},{Scores.Game_Id}\n")'''
				
	def show_top_score(self):
		with open('Scores.txt', 'r') as f:
			sorted_scores = []
			for line in f:
				values = line.strip().split(',')
				username, score, win, Game_Id = values[:4]
				score = int(score)
				win = int(win)
				sorted_scores.append(Scores(username, score, win, Game_Id))
			sorted_scores.sort(key=lambda x: x.score, reverse=True)
			print("Top 10 Scores (Highest Wins):\n")
			for i, score_entry in enumerate(sorted_scores[:10], start=1):
				print(f"{i}. Username: {score_entry.username}, Wins: {score_entry.win}, Score: {score_entry.score}, GameID: {score_entry.Game_Id}")

				
	def load_scores(self):
		self.scores = {}
		if os.path.exists("Scores.txt"):
			with open('Scores.txt', 'r') as f:
				for line in f:
					values = line.strip().split(',')
					username, score, win, game_id = values[:4]
					score = int(score)
					win = int(win)
					if username not in self.scores:
						self.scores[username] = []
					self.scores[username].append(Scores(username, score, win, game_id))
					
	def save_scores(self):
		with open('Scores.txt', 'w') as f:
			for scores in self.scores.values():
				for score_entry in scores:
					f.write(f"{score_entry.username},{score_entry.score},{score_entry.win},{score_entry.game_id}\n")

	def save_and_reset(self, username):
		Game_Id = datetime.datetime.now().strftime("%Y%m%d%H%M")
		if username in self.scores:
			self.scores[username].append[Scores(username, self.score, self.win, Game_Id)]
		else:
			self.scores[username].append[Scores(username, self.score, self.win, Game_Id)]
			self.save_scores()
			self.score = 0
			self.win = 0

	def play_game(self,username):
		Game_Id = datetime.datetime.now().strftime("%Y%m%d%H%M")
		while True:
			round_won=0
			round_loss=0
			print(f"\nStarting game as {username}...")
			for i in range(3):
				player_rolled_dice=Dice_Game.roll_dice()
				print(f"{username} rolled: {player_rolled_dice}")
				cpu_rolled_dice=Dice_Game.roll_dice()
				print(f"CPU rolled: {cpu_rolled_dice}")
				if player_rolled_dice>cpu_rolled_dice:
					print(f"You win this round {username}!")
					round_won+=1
					self.score+=1
				if player_rolled_dice==cpu_rolled_dice:
					print("It's a tie!")
				if player_rolled_dice<cpu_rolled_dice:
					round_loss+=1
					print("Cpu won this round!")
			print("---------------------")
			if round_won>=2:
				self.score += 3
				self.win += 1
				self.scores[username]=Scores(username,self.score,self.win,Game_Id)
				print("You won this stage!")
			elif round_loss>=2:
				print(f"You lost this stage {username}")
			else:
				print("It's a tie!")

			choice1=Inputs(1,"Do you want to continue to the next stage?(1 for Yes,0 for No): ")
			if choice1==0:
				print(f"Total points:{self.score}, Total rounds won:{self.win}")
				self.save_and_reset(username)
				input("Thank you for playing.")
				return
			if choice1==1:
				continue
	def sort_key(self, score,win):
		return (score, win)
	
	def show_top_scores(self):
		sorted_scores = sorted(self.scores.values(), key=lambda x: self.sort_key(x[1], x[2]), reverse=True)
		print("\n\nTop Scores:")
		for rank, score in enumerate(sorted_scores[:10], start=1):
			print(f"{rank}. {score.username}: Score: {score.score}, Stages won: {score.win}")

	def logout(self):
		return
	
	def menu(self,username):
		while True:
			self.load_scores()
			print(f"\nWelcome to the Dice Game {username}")
			print("1. Start Game\n2.Show top scores\n3.Exit")

			choice=Inputs(3,"Enter your choice, or leave blank to cancel:\n")
		
			if choice==1:
				Dice_Game.play_game(self,username)
			if choice==2:
				Dice_Game.show_top_score(self)
			if choice==3:
				return
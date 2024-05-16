from .User import*
from .Score import*
import random

class Dice_Game:
	scores={}
	def roll_dice():
		return random.randint(1,6)
			
	def load_scores(self):
		pass

	def save_scores(self):
		pass

	def play_game(self,username):
		round_won=0
		stage_won=0
		while True:
			print(f"\nstarting game as {username}...")
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
		pass

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
class Dice_Game:

	
	def Inputs(max,message):
		try:
			inputs=int(input(message))
			if inputs>max or inputs<0:
				print("not available, choose a different option")
				print("")
				return inputs
			return
		except ValueError:
			print("not available, choose a different option")
			input()
			return
			
	def __init__(self,username,password,score):
		self.username=username
		self.password=password
		self.score=score

	def load_scores():
		pass

	def save_scores():
		pass

	def play_game():
		pass

	def show_top_scores():
		pass

	def logout():
		pass
	def menu(self):
		print("Welcome to the Dice Game "+ self.username)
		print("1. Start Game\n2.Show top scores\n3.Exit")

		choice= self.Inputs(3,"Enter your choice, or leave blank to cancel: ")
		
		if choice==1:
			self.play_game()
		if choice==2:
			self.show_top_scores()
		if choice==3:
			self.logout()
		
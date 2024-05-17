import datetime
class Users:
	def __init__(self,username,password):
		self.username=username
		self.password=password

def Inputs(max,message):
		try:
			inputs=int(input(message))
			if inputs>max or inputs<0:
				print("not available, choose a different option")
				print("")
			return inputs
		except ValueError:
			print("not available, choose a different option")
			input()
		except KeyError:
			print("not available, choose a different option")
			input()

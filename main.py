#main
from utils import UserManager

manager=UserManager.user_manager

def Inputs(max,message):
    try:
        inputs= int(input(message))
        if inputs > max or inputs < 0:
            print("not available, choose a different option")
            input()
            return
        return inputs
        
    except ValueError:
            print("not available, choose a different option")
            input()
            return
while True:
    print("Welcome to Dice Roll Game!")
    print("1.Register\n2.Log-in\n3.Exit")

    choice= Inputs(3,"Enter your choice, or leave blank to cancel: ")
    if choice==1:
        manager.login(manager)
    if choice==2:
        print("Loggin in\n")#Log_in()
    if choice==3:
        print("Exiting\n")#Exit()

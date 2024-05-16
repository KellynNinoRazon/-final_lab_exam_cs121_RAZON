#main
from utils import UserManager
from utils import User
manager=UserManager.user_manager()


while True:
    print("Welcome to Dice Roll Game!")
    print("1.Register\n2.Log-in\n3.Exit")

    choice=User.Inputs(3,"Enter your choice, or leave blank to cancel: ")
    if choice==1:
        manager.register()
    if choice==2:
        manager.login()
    if choice==3:
        print("Exiting\n")#Exit()

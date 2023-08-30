# # Rock-Paper-Scissors Game
import random
while True:
    print("1 - Rock \n2 - Paper \n3 - Scissors\n4 - Exit\n")

    options=["","Rock","Paper","Scissors"]
    # result=[[0,1,-1],[-1,0,1],[1,-1,0]]

    inp=int(input("Enter The Choice: "))
    if inp==4:
        exit()
    print("Your Choice: ",options[inp])

    com=random.randint(1,3)
    print("Computer Choice: ",options[com])

    if inp==com:
        print("Game Draw")
    elif inp==1 and com==2:
        print("Computer Wins")
    elif inp==1 and com==3:
        print("You Won")
    elif inp==2 and com==1:
        print("You Won")
    elif inp==2 and com==3:
        print("Computer Wins")
    elif inp==3 and com==1:
        print("Computer Wins")
    elif inp==3 and com==2:
        print("You Won")





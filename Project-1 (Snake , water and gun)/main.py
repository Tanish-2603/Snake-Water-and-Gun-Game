"""

-1 for water
0 for gun
1 for snake

snake water and gun game

"""

import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice : ")
youDict = {"s":1,"g":0,"w":-1}
reverseDict = {1:"Snake" , 0:"Gun",-1:"Water"}
you = youDict[youstr]

# by now we have two number i.e "you" and "computer"\

print(f"You Choose {reverseDict[you]} \nComputer Choose {reverseDict[computer]}")

if(computer==you):
    print("Draw")
else:
    if(computer==-1 and you==1):
        print("You Win!")

    elif(computer==0 and you == -1):
        print("You Win!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Invalid choice")

import paints
import random
user_chose = input("Welcome to the rock paper scissors game pleas writ your chose >>>  ").casefold()
computer_chose = random.randint(0, 2)
names = [paints.rock, paints.paper, paints.scissors]
computer_chose_str = names[computer_chose]
if user_chose[0] == "r":
    user_chose = 0
elif user_chose[0] == "p":
    user_chose = 1
elif user_chose[0] == "s":
    user_chose = 2
else:
    print("eror")
    exit()
txt = f"your chose is {names[user_chose]} computer chose is {computer_chose_str} "
if computer_chose - user_chose == 1 or computer_chose - user_chose == -2:
    print(txt + "The computer beet you")
elif computer_chose == user_chose:
    print(txt + "the result is tie")
else:
    print(txt + "you beat the computer")


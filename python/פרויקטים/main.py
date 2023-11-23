#print(ord(""))

'''def upper_func():
    i = 1
    sentence = input("write here a sentence >>> ")
    upper_sentence = chr(ord(sentence[0]) - 32)
    while i < len(sentence):
        if sentence[i - 1] == " ":
            upper_sentence += sentence[i] + chr(ord(sentence[i + 1]) - 32)
            i += 2
        else:
            upper_sentence += sentence[i]
            i += 1


    print(upper_sentence)

upper_func()'''


'''def cipher():
    user_cipher = ""
    user_choice = input("Would you like to write a code? (press 1) or decode a code? (press 2) >>> ")
    if user_choice == "1":
        user_choice_1 = int(input("Type the number of letters you want to use for the offset >>> "))
        user_sentence = input("Enter here the cipher you would like to convert >>> ").casefold()
        for i in user_sentence:
            if i == " ":
                user_cipher += " "
                continue
            if ord(i) + user_choice_1 > 122:
                user_cipher += chr(ord(i) - 26 + user_choice_1)
            else:
                user_cipher += chr(ord(i) + user_choice_1)
        print("the cipher of the sentence is: " + user_cipher)
    else:
        user_choice_1 = int(input("Type the number of letters you want to use for the offset >>> "))
        user_sentence = input("Enter here the cipher you would like to convert >>> ").casefold()
        for i in user_sentence:
            if i == " ":
                user_cipher += " "
                continue
            if ord(i) - user_choice_1 < 97:
                user_cipher += chr(ord(i) + 26 - user_choice_1)
            else:
                user_cipher += chr(ord(i) - user_choice_1)
        print("The original sentence is: " + user_cipher)

cipher()'''
# b = ["a", "b"]
#
# a = [1, b]
# print(a)
# dict = {"a": 1, "b": 2}
# print(dict["a"])
# a = {"a":1, "b": 2}
# b = a
# print(b)
#
# from turtle import Turtle, Screen
#
# timy = Turtle()
# timy.shape("turtle")
# timy.color("green")
# my_screen = Screen()
# my_screen.exitonclick()
#
# print(f"{Turtle} {my_screen}")

# from prettytable import PrettyTable
#
#
# table = PrettyTable()
# table.field_names = (["name", "type"])
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
#
# print(table)

# class Car:
#     seats = 4
#     def __init__(self):
#         pass
#     def enter_race_mode(self):
#         self.seats = 2
# my_car = Car()
# print(my_car.seats)
#
# my_car.enter_race_mode()
# print(my_car.seats)

# class User:
#     user = 0
#     folow = 0
#     def __init__(self):
#         pass
#     def folowers(self, user, folow):
#         self.user += 1
#         self.folow += 1
# user1 = User()
#
# print(user1.user)
# print(user1.folow)


# class User:
#     def __init__(self, userID, username):
#         self.id = userID
#         self.username = username
#
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, whats_his_name):
#         self.following += 1
#         whats_his_name.followers += 1
#
#
# user_1_chaim = User("1234", "Chaim")
# user_2_ben = User("5678", "Benayahu")
#
# user_2_ben.follow(user_1_chaim)
# print(user_2_ben.following)
# print(user_1_chaim.followers)


# from turtle import Turtle, Screen
# from random import choice, randint
# timmy = Turtle()
# color = ["green", "yellow",  "blue", "light blue", "light green"]
# # direction = [90, 270]
# # timmy.pensize(20)
# #
# # while True:
# #     pen_direction = choice(direction)
# #     pen_color = choice(color)
# #     steps = randint(20, 150)
# #     timmy.color(pen_color)
# #     timmy.right(pen_direction)
# #     timmy.forward(steps)
#
#
#
# for j in range(3, 9):
#     pen_color = choice(color)
#     for i in range(j):
#         timmy.color(pen_color)
#         timmy.forward(80)
#         timmy.right(180 - (180 * (j - 2) / j))
#
#
#
# screen = Screen()
#
# screen.exitonclick()
# for i in range(1000000):
#     print(i, end=' ')

# my_tuple = (1, 2, 3)

# from turtle import Turtle, Screen
# from random import randint
#
# def color_mode():
#     rgb = []
#     for i in range(3):
#         color = randint(1, 255)
#         rgb.append(color)
#     rgb = tuple(rgb)
#     return tuple(rgb)
#
# tim = Turtle()
#
# screen = Screen()
# tim.shape("turtle")
# screen.colormode(255)
# # tim.pensize(5)
#
# for j in range(0, 1000):
#     if j % 4 == 0:
#         rgb = color_mode()
#     for i in range(4):
#         tim.speed(99)
#         tim.pencolor(rgb)
#         tim.forward(10 + j)
#         tim.right(90)
#     tim.left(90)
#     tim.forward(10 + j)
#
#
#
#
#
# screen.exitonclick()
# import os
# # from time import sleep
# # space = ""
# # for i in range(100):
# #     sleep(4)
# #     space += " "
# #     print(rf'''{space} ______
# # {space}/|_||_\`.__
# # {space}(   _    _ _\
# # {space}=`-(_)--(_)-'  hjw''', end='\r')

# 20/11/2023

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# screen = Screen()
# screen.setup(width=1250, height=600, startx=0, starty=0)
# user_guess = screen.textinput(title="Hello! Plleas enter your guess", prompt="which turtle will win? (enter a color)")
# print(user_guess)
# screen.exitonclick()

# 21/11/2023

# from math import *
#
#
# from turtle import Screen, Turtle
#
# timmy = Turtle()
# screen = Screen()
#
# def w_letter():
#     timmy.pendown()
#     timmy.right(70)
#     timmy.forward(50)
#     timmy.left(140)
#     timmy.forward(45)
#     timmy.right(140)
#     timmy.forward(45)
#     timmy.left(140)
#     timmy.forward(50)
#     timmy.right(70)
#     timmy.penup()
#     timmy.forward(30)
# def o_letter():
#     timmy.pendown()
#     for i in range(36):
#         timmy.forward(4)
#         timmy.right(10)
#     timmy.penup()
#     timmy.forward(30)
#
# def mark():
#     timmy.pendown()
#     timmy.right(90)
#     timmy.forward(40)
#     timmy.penup()
#     timmy.pensize(5)
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(1)
#     timmy.penup()
#     timmy.backward(50)
#     timmy.left(90)
#     timmy.forward(50)
# w_letter()
# o_letter()
# w_letter()
# mark()
#
#
#
# screen.exitonclick()

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
d = c * 2
print(d)


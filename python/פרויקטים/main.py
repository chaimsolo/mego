# print(ord(""))

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
# # user_guess = screen.textinput(title="Hello! Plleas enter your guess", prompt="which turtle will win? (enter a color)")
# # print(user_guess)
# # screen.exitonclick()
#
# # # 21/11/2023
# #
# # # from math import *
# # #
# #
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
# def a_letter():
#     timmy.pendown()
#     timmy.right(110)
#     timmy.forward(50)
#     timmy.backward(50)
#     timmy.left(40)
#     timmy.forward(25)
#     timmy.right(110)
#     timmy.forward(18)
#     timmy.backward(18)
#     timmy.left(110)
#     timmy.forward(25)
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
#
# a_letter()
# # w_letter()
# # o_letter()
# # w_letter()
# mark()


#
# screen.exitonclick()
# #
# # a = [1, 2, 3]
# # b = [4, 5, 6]
# # c = a + b
# # d = c * 2
# # print(d)
#
# lettres = "abcdefg"
# dic = 123_456
# print(lettres[-4:0:])
# def a(a, b):
#     return a + b
# # a(1)
# a = 2.12345
# b = "{0:.2f} 2.123  12345 {1}".format(a, 1)
# print(b)
#
# for i in range(1, 13):
#     print("no. {:4}, {:4}".format(i, i**2))
# line = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
# print(f"{line[0]}\n{line[1]}\n{line[2]}")
# flag = 1
# while flag:
#     x_or_0 = input("what do you want to paint? (x or 0) >>> ")
#     choice_line = int(input("Enter the line number Where you like to  located your choice >>> ")) - 1
#     choice_row = int(input("Enter the row number Where you like to  located your choice >>> ")) - 1
#     line[choice_line][choice_row] = x_or_0
#     print(f"{line[0]}\n{line[1]}\n{line[2]}")
#     for i in range(3):
#         if line[i][0] == line[i][1] == line[i][2] and line[i][2] != "-" or line[0][i] == line[1][i] == line[2][i] and line[2][i] != "-"\
#                 or line[0][0] == line[1][1] == line[2][2] and line[2][2] != "-" or line[0][2] == line[1][1] == line[2][0] and line[2][0] != "-":
#             print("won")
#             flag = 0
#             break


# def orgeniz_numbers(num):
#     store = []
#     i = 1
#     while num:
#         store
#     return store
#
# num_a = int(input("Enter a number >>>"))
# num_b = int(input("Enter an other number >>>"))
# while num_a:
#
#
# num_a = orgeniz_numbers(num_a)
# num_b = orgeniz_numbers(num_b)
# print(num_a)
# print(num_b)

# print("hello {0:.2f}".format( 2.2222))
# a = "abcd"
# print(a.upper())

# 28/11/2023
# data = "a", "b", "c"
# x, y, z = data
# n_data = data[::-1][::-1]
# print(data)
# print(n_data)
# a = "abc"
# a[0] = "v"
# print(a)
#
# letters = "abcdefghijklmnopqrstuvwxyz"
# print(letters[14:17:-1])
# print(letters[4::-1])
# print(letters[:-9:-1])

# a = "abcd"
# for i in enumerate({"a": "letter a", "b": "letter b"}):
#     print(i)

# class User:
#     def __init__(self, user, username):
#         self.id = user
#         self.username = username
#         # default values
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

# # join method
# dict = {"a":"letter a", "b": "letter b"}
# print("".join(dict))

# # ljust method
# a = "banana"
# print(a.ljust(50, "5"), "is the best food")

# # lower method
# a = "HELLO"
# print(a.lower())

# # lstrip method
# txt = "       banana     "
# print(txt.lstrip(), "is the best food")
#
# # maketrans and translate methods
# txt = "hello  Dan"
# x = "Dan"
# y = "David"
# table = str.maketrans(x, y)
# print(txt.translate(table))

# # shows ascii value of octal base
# txt = "\107"
# print(txt)

# # shows ascii value of hex base
# txt = "\x79"
# print(txt)

# # \f
# txt = "\fhello\f"
# print(txt)

# # how to clear the console screen (doesn't work on the pycharm console)
# import os
# import time
# print("avi")
# time.sleep(2)
# os.system("cls")
# time.sleep(2)
# print("shlomo")

# # checking the name of 'set' varible
# a = {1, 2}
# print(type(a))

# # class that gets a serial number of the objects
# class Number:
#     num_of_objects = 0
#     def __init__(self):
#         Number.num_of_objects += 1
#         self.id = Number.num_of_objects
#     def printingNumberOfObject(self):
#         print(f"The serial number of object is: {self.id}")
#

# list = []
# for i in range(10):
#     number = Number()
#     list.append(number)
# for i in range(10):
#     list[i].printingNumberOfObject()
# print(isinstance(number, Number))

# a = ["a", "b"]
# print(id(a))
# b = "c", "d"
# a [1] = 9
# print(id(a))
# print(a)


# 03/12/2023
# my_set = [1, 4, 2, 6]
# my_set = set(my_set)
# my_set.add(3)
# cars = ["toyote", "mazda"]
# f = open("txt.txt", 'r', encoding="utf-8")
# for u in f:
#     print(u, )


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


class User:
    def __init__(self, userID, username):
        self.id = userID
        self.username = username

        self.followers = 0
        self.following = 0

    def follow(self, whats_his_name):
        self.following += 1
        whats_his_name.followers += 1


user_1_chaim = User("1234", "Chaim")
user_2_ben = User("5678", "Benayahu")

user_2_ben.follow(user_1_chaim)
print(user_2_ben.following)
print(user_1_chaim.followers)

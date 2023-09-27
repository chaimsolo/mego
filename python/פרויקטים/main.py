import random
line = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"], ]
print(line)
print(line)
print(line)
choice_line = []
user_line = int(input(f"pleas enter the place you think their is the treasure"
f"enterthe line number>>> "))
row = int(input("Enter here the row number >>> "))
treasure_line = random.randint(1,4)
treasure_row = random.randint(1,4)
if user_line == treasure_line and row == treasure_row:
    print("Hooray you guessed right!")

    for i in range(1, 4):
        if user_line == i:
            for j in range(1, 4):
                if j == row:
                    choice_line.append("x")
                else:
                    choice_line.append("_")
            print(choice_line)
        else:
            print(line)
else:
    print("You guessed wrong, the treasure was here")

    for i in range(1, 4):
        if treasure_line == i:
            for j in range(1, 4):
                if j == treasure_row:
                    choice_line.append("x")
                else:
                    choice_line.append("_")
            print(choice_line)
        else:
            print(line)

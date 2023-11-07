import random
import gussing_game_img
def checking_guess(guess, number, level):
    if guess == number:
        print(f"The number {guess} is the right number.")
        # in this case the game is ended
        print(f"{gussing_game_img.well_done}, you guessed right.")
        level = 0

    else:
        level -= 1
        if guess < number:
            print(f"The number {guess} is too low.")
        else:
            print(f"The number {guess} is too high.")
    return level

# the number the player needs to guess
number = random.randint(1, 101)
# the number of the attempts. given from the user 1 or 2  and calculate it.
choice = int(input(f"{gussing_game_img.welcome}.\n\n choose which level do you want to play with (easy 1) (hard 2) >>> "))
if choice == 1:
    level = 10
elif choice == 2:
    level = 5

while level > 0:
    guess = int(input(f"You have {level} attempts. Enter here the number >>> "))
    level = checking_guess(guess, number, level)
if number != guess:
    # in this case the game is ended
    print(f"You didn't guess correctly in any of your attempts, try again. the right number was {number}")

input("press enter to exit >>> ")






import random
start = list(input("Welcome to the bankers' roulette enter your the first caracter in your names"))
roulette = random.randint(0, len(start))
print("The banker who has to pay today's name starts with a letter  " + start[roulette])
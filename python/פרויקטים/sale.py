check = 1

while check == 1:
    name = input("What is your name? ")
    price = int(input("What is the price you would like to offer?"))
    repeat = input("Does anyone else want to make an offer?")
    if repeat[0] == "n":
        check = 0
print(f"The winner is {name} with {price} ILS.")
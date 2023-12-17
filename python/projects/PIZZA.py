size_of_pizza = input("Welcome to pizzos What size pizza tray would you like to order? >>>").lower()
mushrooms_and_olives = input("Would you like extra olives and mushrooms? >>>").lower()
olives = input("Would you like a extra of only olives? >>>").lower()
cheese = input("Would you like extra cheese? >>>").lower()
cost = 0
if cheese[0].casefold() == "y":
    cost += 3
if size_of_pizza[0].casefold() == "b" or size_of_pizza == "l":
    cost += 25
    if mushrooms_and_olives[0] == "y":
        cost += 5
    if olives[0] == "y":
        cost += 6
elif size_of_pizza[0] == "m":
    cost += 20
    if mushrooms_and_olives[0] == "y":
        cost += 5
    if olives[0] == "y":
        cost += 4
else:
    cost += 15
    if mushrooms_and_olives[0] == "s":
        cost += 2
    if olives[0].casefold() == "y":
        cost += 2
print(f"Thank you for choosing to order pizza at Pizzos, now you have to pay {cost}"
      f" shekels And within twenty minutes the pizza will be ready.")


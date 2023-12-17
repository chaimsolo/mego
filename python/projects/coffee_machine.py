import coffee_machine_img

# creating dictionaries for the types of coffees and for the machine
cappuccino = {"name": "cappuccino", "watter": 250, "milk": 100, "coffee": 24, "price": 3}
espresso = {"name": "espresso", "watter": 50, "milk": 0, "coffee": 18, "price": 1.5}
latte = {"name": "latte", "watter": 200, "milk": 150, "coffee": 24, "price": 2.5}

money_in_machine = {"penny": 0, "nickel": 0, "dime": 0, "quarter": 0}
coins_in_machine = {"penny": 0, "nickel": 0, "dime": 0, "quarter": 0}
coins = {"penny": 0.01, "nickel": 0.05, "dime": 0.1, "quarter": 0.25}

machine_resources = {"watter": 300, "milk": 200, "coffee": 100}
copy_machine_resources = {"watter": 300, "milk": 200, "coffee": 100}

# creating a list to manage the dictionaries
list_of_coffee = [cappuccino, espresso, latte]
list_of_machine = [money_in_machine, coins_in_machine, machine_resources]


# a function for calculating the sum of dollars by gating the number and types of coins
def coins_func():
    sum = 0
    for coin in coins:
        coins_of_user = int(input(f"\nEnter in how meny {coin} would you like to put >>> "))
        coins_in_machine[coin] += coins_of_user
        money_in_machine[coin] += coins_of_user * coins[coin]
        sum += coins_of_user * coins[coin]
    return sum

# a function that removing the change from the machine
def removing_coins_from_machine(sum):
    for coin in coins_in_machine:
        #t his is for a case there is not enough resources and the machine returning all of the money
        if check == 0:
            while coins_in_machine[coin] > 0 and sum > 0:
                sum = round(sum - coins[coin], 2)
                coins_in_machine[coin] -= 1
                money_in_machine[coin] -= round(coins[coin], 2)
        else:
            while coins_in_machine[coin] > 0 and sum > price_of_coffe:
                sum = round(sum - coins[coin], 2)
                coins_in_machine[coin] -= 1
                money_in_machine[coin] -= round(coins[coin], 2)

# a function that checking the resources of the machine
def resources_of_machine():
    for resource in machine_resources:
        machine_resources[resource] -= list_of_coffee[start][resource]
        if machine_resources[resource] < 0:
            machine_resources[resource] += list_of_coffee[start][resource]
            print(f'''Sorry but the machine doesn't have enough materials for your {name_of_coffee},
Here is your money back, {sum} dollars.
However you can choose a different type of coffee''')
            return 0
    print(f'''You put {round(sum, 2)} dollars in the machine,
The price is {price_of_coffe},
therefore the machine returning now {change} dollars
And here is your coffee.
    {coffee_machine_img.coffee_cup}''')
    return 1


# a function for the technic who is adding resources
def adding_resources():
    for resource in machine_resources:
        add_resource = int(input(f'''Enter here how much ML/gram would you like to add to {resource}'''))
        machine_resources[resource] += add_resource


def technic_mode():
    while True:
        technic_menu = int(input('''pleas fallow the instructions carefully.
for the report about the money inside the machin press 1
for the report about the type of coins inside the machin press 2
for the report about the resources inside the machin press 3
to add money press 4
to add resources press 5
>>> ''')) - 1
        if 0 <= technic_menu < 3:
            print(list_of_machine[technic_menu])
        elif technic_menu == 3:
            coins_func()
        elif technic_menu == 4:
            adding_resources()
        repeat_technic_mode = int(input("Would you like to go back to the main menu (press  1) or to the technic menu (press 2)"))
        if repeat_technic_mode == 1:
            return


while True:
    # the beginning of program
    start = int(input(coffee_machine_img.welcome + "\n\nChoose your beverage (cappuccino 1) (espresso 2) (latte 3) >>> ")) - 1
    while True:
        # a case of entering the technic mode
        if start == 1233:
            technic_mode()
            sum = 0
            start = int(input(coffee_machine_img.welcome + "\n\nChoose your beverage (cappuccino 1) (espresso 2) (latte 3) >>> ")) - 1
        else:
            break



    # vars of the price and the name of the specific coffe
    price_of_coffe = list_of_coffee[start]["price"]
    name_of_coffee = list_of_coffee[start]["name"]

    print(f'''You chose the {name_of_coffee},
Now you need to put in the machine {price_of_coffe} dollars.
You need to write which coin do you want to put in, And hou many from each coin''')

    # first use of the coins function
    sum = round(coins_func(), 2)

    while True:
        # this is saving the memory values of the machine resources for a case there is not enough resource, and the machine won't lose it.
        for resource in machine_resources:
            copy_machine_resources[resource] = machine_resources[resource]

        change = round(sum - price_of_coffe, 2)

        if sum == price_of_coffe:
            # this returning weather 0 or 1 to check if there is enough resources.
            check = resources_of_machine()
            removing_coins_from_machine(sum)
            break

        elif sum > price_of_coffe:
            check = resources_of_machine()
            removing_coins_from_machine(sum)
            break

        else:
            repeat = input(f'''\n\nYou didn't put in enough money, You steel need {round(price_of_coffe - sum, 2)} dollars
            
would you like to put more money (press 1) or to get back the money you have put already? (press 2 or any button) >>> ''')
            if repeat[0] == "1":
                sum += round(coins_func(), 2)

            else:
                print(f'''\n\nyou choose to get your money back. 🤔mmmm.... one minute i'm calculating.

Here is your money 💰
{sum}''')
                check = 0
                break
    # this is for the case there was not enough resources and the machine's memory is returning back to the beginning
    if check == 0:
        machine_resources = copy_machine_resources

    turn_of = input("\n\nWould you like to turn of the machine? >>> ")
    if turn_of[0] == "y":
        break
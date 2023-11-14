from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from coffee_machine_img import welcome

while True:

    start_menu = Menu()
    making_coffee = CoffeeMaker()
    making_money = MoneyMachine()

    name_user_chose = input(f'''{welcome}
choose the type of coffe you want to order {start_menu.get_items()} >>> ''')
    if name_user_chose == "1234":
        technic = int(input("Enter 1 for financial reports or 2 for resources report >>> "))
        if technic == 1:
            making_money.report()
        elif technic == 2:
            making_coffee.report()
    else:
        coffee_object = start_menu.find_drink(name_user_chose)


        making_coffee.is_resource_sufficient(coffee_object)

        print(f'''The price for {coffee_object.name}  is: {coffee_object.cost} ''')

        if making_money.make_payment(coffee_object.cost) == True:
            making_coffee.make_coffee(coffee_object)
    turn_of = input("Would you like to turn of the machine? >>> ")
    if turn_of[0] == "y":
        break



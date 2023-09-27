# input vars
name = input("Hello, Welcome to our tip calculator. What is your name?\n")
bill = int(input("What is the sum of the bill? \n"))
tip = int(input("What percentage of the bill do you want to give as a tip? \n"))
participants = int(input("How meny people are dining? \n"))
# calculation
total_bill = bill * tip / 100 + bill
cost_per_participant = total_bill / participants
final_cost_per_participant = "{:.2f}".format(cost_per_participant)
# print
print(f'''{name}, The amount you have to pay for the meal is {bill} ILS, 
The percentage of the tip you chose to give is {tip}%, 
The number of diners is {participants}, Therefore each diner must pay {final_cost_per_participant} ILS.


    ''')
# this eלnd var is to prevent Automatic closing of the program
end = input("Press enter to close the program")
turn = ["first", "second", "third"]
numbers_checking = ["even", "odd"]
PI = 3.141592653589793

# first function
def sum_of_numbers():
    sum = 1
    for i in range(3):
        number = int(input(f"Enter the {turn[i]} number >>> "))
        sum *= number
    print(f"The multiplication result of the three numbers is: {sum}")
# second function

def full_name():
    name = []
    for i in range(2):
        name.append(input(f"Enter here your {turn[i]} name >>> "))
    print(f"your full name is {name[0]} {name[1]}.")

# third function

def biggest_number():
    for i in range(3):
        number = int(input(f"Enter here the {turn[i]} number >>> "))
        if i == 0 or number > high_number:
            high_number = number

    print(f"The number with the highest value is: {high_number}.")

# fourth function

def long_student_name():
    long_name = ""
    for i in range(3):
        name_of_student = input(f"Enter here the name of the {turn[i]} student >>> ")
        if len(name_of_student) > len(long_name):
            long_name = name_of_student
    print("The student with the longest name is: " + long_name + ".")

# fifth function

def even_or_odd():
     number = int(input("Enter here the number >>> "))
     print(f"the number you have entered is an {numbers_checking[number % 2]} number.")

# sixth function

def area_of_circle():
    radius = int(input("Enter here the length of the radius >>> "))
    area = round(PI * radius ** 2, 2)
    print(f"The area of the circle is: {area}")

function_selection = int(input("Select which function number you want to activate >>> "
                               ""))

if function_selection == 1:
    sum_of_numbers()
elif function_selection == 2:
    full_name()
elif function_selection == 3:
    biggest_number()
elif function_selection == 4:
    long_student_name()
elif function_selection == 5:
    even_or_odd()
elif function_selection == 6:
    area_of_circle()
else:
    print("The function number you entered does not exist")




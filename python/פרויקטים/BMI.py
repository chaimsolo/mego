age = int(input("Enter your age >>>"))
weight = float(input("Enter your weight >>>"))
height = float(input("Enter your height >>>"))


#calculation
bmi = round(weight / height**2, 2)
bmi1 = f"your bmi is {bmi}. you are Underweight!!!"
bmi2 = f"your bmi is {bmi}. you are in a proper weight."
bmi3 = f"your bmi is {bmi}. you are in a overweight."
bmi4 = f"your bmi is {bmi}. you are in a obesity."
obese_value = 30
if age >= 65:
    if age < 75:
        if bmi < 22:
            print(bmi1)
        elif bmi < 27:
            print(bmi2)
        elif bmi < obese_value:
            print(bmi3)
        else:
            print(bmi4)
    else:
        if bmi <= 23:
            print(bmi1)
        elif bmi < 28:
            print(bmi2)
        elif bmi < obese_value:
            print(bmi3)
        else:
            print(bmi4)
else:
    if bmi < 18.5:
        print(bmi1)
    elif bmi < 25:
        print(bmi2)
    elif bmi < obese_value:
        print(bmi3)
    else:
        print(bmi4)
import calculater_img
quistion = "y"
while quistion[0] == "y":
    numbers = input(f"{calculater_img.img}\n\n"
                "enter the numbers with the action you would like to do with space between them >>> ")
    numbers = numbers.split(" ")
    number1 = float(numbers[0])
    number2 = float(numbers[2])
    def addition(number1, number2):
        return number1 + number2

    def substraction(number1, number2):
        return number1 - number2

    def multiplication(number1, number2):
        return number1 * number2

    def devision(number1, number2):
        return number1 / number2

    if numbers[1] == "+":
        result = addition(number1, number2)
    elif numbers[1] == "-":
        result = substraction(number1, number2)
    elif numbers[1] == "*":
        result = multiplication(number1, number2)
    elif numbers[1] == "/":
        result = devision(number1, number2)

    quistion = input(f"The tesult is: {result} \n\nwould you like to calculate another thing? ")
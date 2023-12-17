height = int(input("what is your height in centimeters? >>> "))
age = int(input("what is your age? >>> "))
if height >= 150:
    if age < 18:
        if age >= 12:
            photo = (input("Would you like to take a photo? >>> "))
            if photo[0].casefold() == "y":
                price_of_photo = "And you need to pay 5 NIS for the photo."
            else:
                price_of_photo = ""
            print("You are allowed to enter the Anaconda facility and you must pay NIS 25. " + price_of_photo)
        else:
            print("You are only allowed to enter the zoo, and you have to pay 10 shekels for that.")
    else:
        if age <= 55 and age >= 40:
            print("You are allowed to enter the Anaconda facility for free. ")
        else:
            photo = (input("Would you like to take a photo? >>> "))
            if photo[0].casefold() == "y":
                price_of_photo = "And you need to pay 5 NIS for the photo."
            else:
                price_of_photo = ""
            print("You are allowed to enter the Anaconda facility and you must pay NIS 30. " + price_of_photo)
else:
    if age < 18:
        print("You are only allowed to enter the zoo, and you have to pay 10 shekels for that.")
    else:

        print("You are allowed to enter the electric cars"
              ", for that you have to spend NIS 20 from your pocket. ")


input("Press Enter to finish th program")
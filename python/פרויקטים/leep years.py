year = int(input("Enter the year number here >>> "))
leap = "The year you have entered is a leap year."
not_leap = "The year you have entered isn't a leap year."
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(leap)
        else:
            print(not_leap)
    else:
        print(leap)
else:
    print(not_leap)
input("Press enter to exit >>>")
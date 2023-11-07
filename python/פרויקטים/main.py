#print(ord(""))

'''def upper_func():
    i = 1
    sentence = input("write here a sentence >>> ")
    upper_sentence = chr(ord(sentence[0]) - 32)
    while i < len(sentence):
        if sentence[i - 1] == " ":
            upper_sentence += sentence[i] + chr(ord(sentence[i + 1]) - 32)
            i += 2
        else:
            upper_sentence += sentence[i]
            i += 1


    print(upper_sentence)

upper_func()'''


'''def cipher():
    user_cipher = ""
    user_choice = input("Would you like to write a code? (press 1) or decode a code? (press 2) >>> ")
    if user_choice == "1":
        user_choice_1 = int(input("Type the number of letters you want to use for the offset >>> "))
        user_sentence = input("Enter here the cipher you would like to convert >>> ").casefold()
        for i in user_sentence:
            if i == " ":
                user_cipher += " "
                continue
            if ord(i) + user_choice_1 > 122:
                user_cipher += chr(ord(i) - 26 + user_choice_1)
            else:
                user_cipher += chr(ord(i) + user_choice_1)
        print("the cipher of the sentence is: " + user_cipher)
    else:
        user_choice_1 = int(input("Type the number of letters you want to use for the offset >>> "))
        user_sentence = input("Enter here the cipher you would like to convert >>> ").casefold()
        for i in user_sentence:
            if i == " ":
                user_cipher += " "
                continue
            if ord(i) - user_choice_1 < 97:
                user_cipher += chr(ord(i) + 26 - user_choice_1)
            else:
                user_cipher += chr(ord(i) - user_choice_1)
        print("The original sentence is: " + user_cipher)

cipher()'''
b = ["a", "b"]

a = [1, b]
print(a)

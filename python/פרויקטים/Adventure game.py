import bassement_images
start1 = f'''{bassement_images.beer_basement}\n\nYou are in a beer basement.
In front of you there is two barrels,
in one of them there is an instruction
for the shortest way to get out of the place,
if you open the second barrel you will get money. press A to the
first barrel or B for the second barrel >>> '''

dove_chapter1 = f'''\n\n\n\n{bassement_images.barrel}\n\n\n\nVery nice. You chose the right barrel,
a white dove is hiding inside the barrel,
if you write here the symbol it represents,
so the barrel will opened >>> '''

lights_chapter1 = f'''\n\n\n\n{bassement_images.white_dove}\n\nvery true. This is the correct answer.
the white dove came out and she turn on the lights.
Now when the lights in the room come on
you are seeing here someone else who
is currently sleeping on the other side of the room,
would you like to wake him up? >>> '''

scary_chapter1 = f'''\n\n\n\n{bassement_images.angry_man}\n\nYou woke up the person,
ummm, it turns out that he's
drunk because he drank some beers, now he's angry
because of you, because you woke him up, and he's one of
those noisy people who aren't clear,
you have two options fight him or try to run away,
would you like to fight(press A) or run away(press B)?'''

two_options_str = '''\n\n\n\nYou chose to fight, but now the man has
sobered up from his drunkenness, and he wants to
offer you help on how to get out, it turns out that
the key to the basement is on the ceiling,
which is as high as two people, you must offer
a possible solution from two options.
1. Take the two barrels and then climb over both
2. Make a thieves ladde'''

two_options_result_2 = '''\n\n\n\nWell done, after many efforts you managed
to get out of the basement,
now you have a new life friend,
go out, drink beer and enjoy yourself.'''

two_options_result_1 = '''\n\n\n\nThis is the wrong answer.
you've almost reached the end,
but it's okay, you always can start from the beginning'''

scary_chapter2 = '''\n\n\n\nYou chose the wrong path,
you have to fight, now you have to start
all over again.'''

lights_chapter2 = '''\n\n\n\nSorry but you didn't answer the riddle correctly,
now you can only drink beers and wait until
someone comes to take you out.'''

dove_chapter2 = '''\n\n\n\nSorry but this is not a correct answer,
you have to start from the beginning'''

start2 = f'''\n\n\n{bassement_images.money_image}\n\n\n\nYou have now received 100000% dollars,
you have to choose whether you want to donate all
the money to charity (press A), or whether to buy the basement(press B).'''

money1 = '''\n\n\n\nYou chose to donate the money to charity,
very nice. Now tap \"charity cup\" to find where to put it.'''

charity1 = '''\n\n\n\nDo you see the cup of charity there?
Congratulations, you can now get out of the basement
if you just pick up the cup, just don't forget to
put the money there.'''

charity2 = '''\n\n\n\nSorry but now you are stuck here,
you had a chance and you didn't take it'''

money2 = '''\n\n\n\nVery nice, now that the basement belongs to you,
         the cellar workers will come quickly to rescue you,
          and now you are out.'''

classic_error = '''\n\n\n\nYou have entered a character that is not
included according to the rules of the game,
now you need to start from the beginning.'''




start = input(start1).casefold()

if start == "a":
    dove_chapter = input(dove_chapter1).casefold()
    if dove_chapter[0] == "p":
        lights_chapter = input(lights_chapter1).casefold()
        if lights_chapter[0] == "y":
            scary_chapter = input(scary_chapter1).casefold()
            if scary_chapter[0] == "a":
                two_options = input(two_options_str).casefold()
                if two_options == "2":
                   print(two_options_result_2)
                elif two_options == "1":
                   print(two_options_result_1)
                else:
                    print(classic_error)
            elif scary_chapter[0] == "b":
                print(scary_chapter2)
            else:
                print(classic_error)
        elif lights_chapter[0] == "n":
            print(lights_chapter2)
        else:
            print(classic_error)
    else:
        print(dove_chapter2)
elif start == "b":
    money = input(start2).casefold()
    if money == "a":
        charity = input(money1).casefold()
        if charity[0] == "c":
            print(charity1)
        else:
            print(charity2)
    elif money == "b":
        print(money2)
    else:
        print(classic_error)
else:
    print(classic_error)







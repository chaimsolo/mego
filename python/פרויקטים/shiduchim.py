man_name = input("Enter the guy name >>>").lower()
woman_name = input("Enter the lidy name >>> ").lower()
man_name_and_woman_name = man_name + woman_name
len_of_man_name_and_woman_name = len(man_name) + len(woman_name)
t = man_name_and_woman_name.count("t")
r = man_name_and_woman_name.count("r")
u = man_name_and_woman_name.count("u")
e = man_name_and_woman_name.count("e")
l = man_name_and_woman_name.count("l")
o = man_name_and_woman_name.count("o")
v = man_name_and_woman_name.count("v")
sum = t + r + u + e + l + o + v
mach_percentage = round((sum / len_of_man_name_and_woman_name) * 100, 2)
verbel_mach_percentage = f"the percentage of mach is {mach_percentage}% "
if mach_percentage <= 10:
    print(verbel_mach_percentage + " Ummm... not so appropriate, try looking for someone else, or change the names")
elif mach_percentage <= 60:
    print(verbel_mach_percentage + "You might have to work on your Human qualities together, but try, why not actually.")
elif mach_percentage <= 99:
    print(verbel_mach_percentage + "This could be your one, go for it.")
else:
    print(verbel_mach_percentage + "Congratulations, you are in a complete match.")
input("Press enter to exit")


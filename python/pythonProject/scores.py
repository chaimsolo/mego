import math

a = int(input('enter your magen score:'))
b = int(input('enter your mahat score:'))
av = ((a+b)/2)
av = math.ceil(av)
ana = ("You didn't pass the test, but don't be upset, try again.")
gap = a-b
seenb = gap>20
senrioa = (b>=40 and b<=54)
if b<0 or a<0:
    print('Here is a system for calculating scores. Not a standup club!!!')
elif a<55 or b<40 or av<55:
    print (ana)
elif senrioa and seenb and av>54:
    print('your score is 55!')
else:
    print('your final score is:',av)
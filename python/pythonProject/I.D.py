id = (input('Enter your I. D. number:\n'))
a = 0
for i in range(len(id)):
    if i % 2 == 0:
        a += int(id[i])
    else:
        a += int(id[i]) * 2 // 10 + int(id[i]) * 2 % 10
print((100 - a) % 10)
#if (a + int(id[-1])) % 10 == 0:
    #print('You submitted a valid ID')
#else:
    #print('Your ID is not valid!!!!')


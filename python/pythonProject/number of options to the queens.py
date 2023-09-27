a = []
b = 0
c = 0
d = 0
e = 1
f = 0
for i in range(8):
    b = input()
    a.append(b[0])
    a.append(b[2])
for j in range(16):
    c += int(a[j])
for s in range(0, 16, 2):
    d = int(a[s]) + int(a[s + 1])
    for t in range(0, 16, 2):
        e = int(a[t]) + int(a[t + 1])
        if e == d and t != s:
            f += 1
if f != 0 or c != 72:
    print('YES')
else:
    print('NO')

s = open('9.txt').readline()

ma = k = 0
flag = True
my = ['12A', '21A', '11A', '22A', '12B', '21B', '11B', '22B']

for i in range(0, len(s) - 2, 3):
    tri = s[i:i + 3]
    if tri in my:
        flag = True
    else:
        flag = False
    if flag:
        k += 1
    else:
        if k > ma:
            ma = k
        k = 0

print(ma)
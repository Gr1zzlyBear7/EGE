s = open('8.txt').readline()

my = ['BA', 'BO', 'CA', 'CO', 'DA', 'DO']

flag = True
ma = k = 0

for i in range(0, len(s) - 1, 2):
    dva = s[i:i + 2]
    if dva in my:
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
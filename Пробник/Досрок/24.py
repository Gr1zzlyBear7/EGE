from re import *
s = open('24_21421.txt').readline()

num = r'([123456789AB][0123456789AB]+)'
reg = rf'(?=({num}))'
arr = sorted([x.group(1) for x in finditer(reg, s)], key=len, reverse=True)
for x in arr:
    if int(x, 12) % 2 == 0:
        print(len(x))
        break
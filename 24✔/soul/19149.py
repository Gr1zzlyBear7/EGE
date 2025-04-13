from re import *

s = open('19149.txt').readline()

num = r'([1-4]+)'
reg = rf'\({num}([+]{num})+\)'
arr = (sorted([(x.group()) for x in finditer(reg, s)], key=lambda x: -len(x)))
for x in arr:
    if (eval(x)) % 2 == 0:
        print(len(x))
        break
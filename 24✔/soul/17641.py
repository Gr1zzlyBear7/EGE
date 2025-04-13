from re import *

s = open('17641.txt').readline()

num = r'([1-9][0-9]*|0)'
reg = rf'{num}([+*]{num})+'
reg = rf'(?=({reg}))'
arr = sorted([x.group(1) for x in finditer(reg, s)], key=lambda x: -len(x))
for x in arr:
    if eval(x) == 0:
        print(len(x))
        break
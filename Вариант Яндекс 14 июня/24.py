from re import *
s = open('24 (21).txt').readline()

s1 = r'E[ND]*E'
reg = rf'(?=({s1}))'
arr = sorted([x.group(1) for x in finditer(reg, s)], key=len, reverse=True)
for x in arr:
    print(x, len(x))
    input()
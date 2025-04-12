from re import *

s = open('name').readline()

num = r'([1-2][0-2]*|0)'

reg = rf'{num}([*+]{num})+'
reg = rf'(?=({reg}))'
print(max([len(x.group(1)) for x in finditer(reg, s)]))

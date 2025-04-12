from re import *

s = open('name').readline()

reg = r'(YZZ|XY|XZ)+'
reg = rf'(?=({reg}))'

print(max([len(x.group(1)) for x in finditer(reg, s)]))

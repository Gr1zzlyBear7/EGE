from re import *

s = open('27.txt').readline()

reg = '(YZ|Z){0,1}(XYZ)+(XY|X){0,1}'
reg = rf'(?=({reg}))'

print(max([len(x.group(1)) for x in finditer(reg, s)]))
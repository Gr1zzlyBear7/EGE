from re import *

s = open('name').readline()

reg = r'([123][ABC][123])+'
reg = rf'(?=({reg}))'

print(max([len(x.group(a)) // 3 for x in finditer(reg, s)]))

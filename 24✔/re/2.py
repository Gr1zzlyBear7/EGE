from re import *

s = open('name').readline()

reg = r'(ZX|ZY)+'
print(max([len(x.group()) // 2 for x in finditer(reg, s)]))

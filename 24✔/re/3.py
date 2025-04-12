from re import *

s = open('name').readline()

reg = r'([BCD][AO])+'

print(max([len(x.group()) // 2 for x in finditer(reg, s)]))
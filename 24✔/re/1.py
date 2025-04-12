from re import *

s = open('name').readline()
reg = r'[ABC]+'
# for x in finditer(reg, s):
#     print(x.group())

print(max([len(x.group()) for x in finditer(reg, s)]))
from re import *

s = open('name').readline()

num = r'([1-9][0-9]*|0)'

reg = rf'AF{num}([+*]{num})+'

print(max([len(x.group()) for x in finditer(reg, s)]))

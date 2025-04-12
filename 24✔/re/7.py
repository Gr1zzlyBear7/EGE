from re import *

s = open('name').readline()

num = r'([1-9][0-9]*)'

reg = rf'{num}([-*]{num})+'
reg = rf'(?=({reg}))'
print(max([len(x.group(1)) for x in finditer(reg, s)]))
from re import *

s = open('name').readline()

reg = r'(?=((AA|CC)+))'

reg2 = r'(AA|CC)+'
reg2 = rf'(?=({reg2}))'

print(max([len(x.group(1)) // 2 for x in finditer(reg2, s)]))

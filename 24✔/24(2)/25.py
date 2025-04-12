from re import *
s = open('25.txt').readline()

reg = r'(CA)+[AC]{0,1}'
reg = rf'(?=({reg}))'

print(max([len(x.group(1)) for x in finditer(reg, s)]))
from re import *

s = open('26.txt').readline()

reg = r'(DBAC)+(DBA|DB|D){0,1}'

reg = rf'(?=({reg}))'
print(max([len(x.group(1)) for x in finditer(reg, s)]))
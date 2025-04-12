from re import *

s = open('name').readline()

num = r'([1-9][0-9]*|0)'

proiz = rf'(({num}\*)*0(\*{num})*)'

reg = rf'(?=(({proiz}\+{proiz})+))'

print(max([len(x.group(1)) for x in finditer(reg, s)]))

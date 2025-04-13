from re import *

s = open('24_21161.txt').readline()
word = r'([ABCabc][abc]*)'
reg = rf'[ABC][abc]*( {word})*\.'
reg = rf'(?=({reg}))'
m = [x.group(1) for x in finditer(reg, s)]
print(max(m, key=len), len(max(m, key=len)))

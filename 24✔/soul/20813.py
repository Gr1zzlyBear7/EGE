from re import *
s = open('24_20813.txt').readline()

num = r'([789][0789]*|0)'
reg = rf'{num}([-*]{num})+'
reg = rf'(?=({reg}))'
arr = [x.group(1) for x in finditer(reg, s)]
print(max(arr, key=len), len(max(arr, key=len)))
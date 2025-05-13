from re import *
s = open('24_21908.txt').readline()

num = r'[123456789ABCD][0123456789ABCD]*[02468AC]'
reg = rf'(?=({num}))'

arr = [x.group(1) for x in finditer(reg, s)]
arr.sort(key=len, reverse=True)
print(len(arr[0]))
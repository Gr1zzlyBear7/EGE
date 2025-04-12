from re import finditer

s = open('24_19969.txt').readline()
reg = '(?=([a-z]+@[a-z]+\.[a-z]+))'

print(max([len(x.group(1)) for x in finditer(reg, s)]))
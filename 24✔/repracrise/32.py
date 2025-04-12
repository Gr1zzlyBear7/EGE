from re import finditer

s = open('32.txt').readline()
num = r'([1-9][0-9]*[05]+|0)'

reg = rf'(?=({num}([*+]{num})+))'

print(max([len(x.group(1)) for x in finditer(reg, s)]))
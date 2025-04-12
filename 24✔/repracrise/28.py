from re import finditer
s = open('24_18597.txt').readline()
num = r'([1-9]{1}[0-9]{3}\.[0-9]+)+'

reg = rf'(?=({num}(&{num})+))'
print(max([len(x.group(1)) for x in finditer(reg, s)]))
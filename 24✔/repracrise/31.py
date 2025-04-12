from re import finditer

s = open('31.txt').readline()
# s = '0+1130+4625610224014'
num = r'([1-5][0-5]*|0)'
reg = rf'{num}([+*]{num})+'

print(max([len((x.group())) for x in finditer(reg, s)]))
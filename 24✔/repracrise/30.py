from re import finditer

s = open('24_19967.txt').readline()
num = r'(AFD[1-9][0-9]*)'
reg = rf'{num}([+*][1-9][0-9]*|[+*]0)+'
print(max([len(x.group()) for x in finditer(reg, s)]))
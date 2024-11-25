string = open('6.txt').read()
while 'XIXIX' in string: string = string.replace('XIXIX', 'XIX XIX')
print(string.count('XIX'))
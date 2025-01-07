string = open('6.txt').read()
while 'XXXXX' in string:
    string = string.replace('XXXXX', 'XXXX XXXX')
print(string.count('XXXX'))
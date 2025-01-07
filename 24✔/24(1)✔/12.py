string = open('12.txt').readlines()
k = 0
for i in string:
    while 'OAOA' in i: i = i.replace('OAOA', 'OAO AOA')
    if i.count('AOA') > i.count('OAO'):
        k += 1
print(k)
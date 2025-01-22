s = open('24 (17).txt').readline()
while 'ABAB' in s:
    s = s.replace('ABAB', 'ABA B')
while 'BABA' in s:
    s = s.replace('BABA', 'BAB A')

s = s.replace('ABA', '*').replace('BAB', '*')
k = 0
maxi = 0
for let in s:
    if let == '*':
        k += 1
    elif let == ' ':
        pass
    else:
        maxi = max(k, maxi)
        k = 0
print(maxi)
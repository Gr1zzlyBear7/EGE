s = open('24 (16).txt').readline()
while '3' in s:
    s = s.replace('3', 'e')
while '4' in s:
    s = s.replace('4', 'a')
while 'yandex' in s:
    s = s.replace('yandex', '*')

ch = 0
maxi = 0
for let in s:
    if let == '*':
        ch += 1
    else:
        maxi = max(maxi, ch)
        ch = 0
print(maxi * 6)
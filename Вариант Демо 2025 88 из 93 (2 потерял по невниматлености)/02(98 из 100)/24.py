s = open('24 (19).txt').read()
s = s.replace('*', '-')
for x in '678':
    s = s.replace(x, '9')
while '--' in s:
    s = s.replace('--', '- -')
while '00' in s:
    s = s.replace('00', '0 0')
while '09' in s:
    s = s.replace('09', '0 9')
arr = sorted(s.split(), key=len, reverse=True)
for i in arr:
    print(i, len(i))
    input()
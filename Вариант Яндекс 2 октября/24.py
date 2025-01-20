s = open('24 (14).txt').read()
volwes = list('AEIOUY')
ans = []
start = fin = 0
for i in range(len(s) - 1):
    if s[i] in volwes:
        ans.append(len(s[start:fin + 1]))
        start = fin = i
    else:
        fin += 1
ans.append(len(s[start:]))
print(max(ans))

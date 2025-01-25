s = open('15.txt').readline()
ans = []
k = 0
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == 'BB' or s[i] + s[i + 1] == 'DD':
        k += 2
    else:
        ans.append(k)
        k = 2
print(max(ans))
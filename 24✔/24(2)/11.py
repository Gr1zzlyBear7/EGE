s = open('11.txt').readline()

k = ma = 1
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        k += 1
    else:
        if k > ma:
            ma = k
        k = 1

print(ma)
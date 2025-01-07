s = open('13.txt').readline()

k = ma = 1
for i in range(len(s) - 1):
    if s[i] < s[i + 1]:
        k += 1
    else:
        if k > ma:
            ma = k
        k = 1
print(ma)
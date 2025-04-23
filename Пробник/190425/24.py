s = open('24_21717.txt').readline()

k = st = 0
mini = 1000000000000
for i in range(2, len(s)):
    if s[i - 2] + s[i - 1] + s[i] == 'RSQ':
        k += 1
    while k == 130:
        try:
            if s[i + 1] != 'Q':
                mini = min(mini, i + 1 - st + 1)
                if s[st] + s[st + 1] + s[st + 2] == 'RSQ':
                    k -= 1
                st += 1
            else:
                if s[st] + s[st + 1] + s[st + 2] == 'RSQ':
                    k -= 1
                st += 1
        except:
            break
mini = min(mini, i + 1 - st + 1)
print(mini)
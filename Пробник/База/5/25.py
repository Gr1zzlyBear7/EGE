from fnmatch import fnmatch
k = 0
for i in range(0, 10 ** 9 + 1, 21):
    s = list(str(i))
    for x in range(len(s) - 1):
        if s[x] < s[x + 1]:
            pass
        else:
            break
    else:
        if fnmatch(str(i), '1*5*9'):
            print(i, i // 21)
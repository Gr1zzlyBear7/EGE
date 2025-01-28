from fnmatch import fnmatch

k = 0
for i in range(0, 10 ** 9 + 1, 28):
    if fnmatch(str(i), '6323*353?'):
        print(i, i // 28)
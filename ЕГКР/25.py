from fnmatch import fnmatch

k = 0
for i in range(0, 10 ** 10, 18579):
    if fnmatch(str(i), '54?1?3*7'):
        print(i, i // 18579)
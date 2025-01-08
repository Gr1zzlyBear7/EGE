from fnmatch import fnmatch

for i in range(0, 10 ** 6, 51):
    if fnmatch(str(i), '12*45*'):
        print(i, i // 51)
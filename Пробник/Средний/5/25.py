from fnmatch import fnmatch
k = 0
for i in range(1000000000, 100000000, -1):
    if i % 19 == 0 and i % 6 == 0 and i % 2023 == 0:
        if fnmatch(str(i), '1*1*1?'):
            print(i)
            k += 1
    if k == 5:
        break
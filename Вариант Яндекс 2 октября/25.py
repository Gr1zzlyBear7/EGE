from fnmatch import fnmatch

k = 0
for i in range(2 * 10 ** 8, -1, -1):
    if fnmatch(str(i), '?2*4*0') and not fnmatch(str(i), '1*7*') and i % 42 == 0:
        k += 1
        print(i, i // 42)
    if k == 5:
        break
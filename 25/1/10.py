from fnmatch import fnmatch

k = 0
for i in range(700_000, 10 ** 100):
    if not fnmatch(str(i), '*0??3*') and not fnmatch(str(i), '*4??2') and not fnmatch(str(i), '*1*'):
        if i % 13 == 0:
            print(i, sum(map(int, list(str(i)))))
            k += 1
    if k == 5:
        break
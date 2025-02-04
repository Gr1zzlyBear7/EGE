from fnmatch import *

for i in range(0, 10 ** 10 + 1, 21025):
    ev = [x for x in str(i) if int(x) % 2 == 0]
    odds = [x for x in str(i) if int(x) % 2 == 1]
    if len(ev) == len(odds):
        if fnmatch(str(i), '12*34?5'):
            print(i, i // 21025)

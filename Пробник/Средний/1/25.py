from fnmatch import *

for i in range(0, 10 ** 12 + 1, 98591):
    if fnmatch(str(i), '12?3*456??9'):
        print(i, i // 98591)
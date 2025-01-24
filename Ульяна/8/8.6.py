from itertools import *

k = 0
arr = list(product('ЕКОФ', repeat=5))
print(arr.index(tuple('ФФФЕО')) + 1)

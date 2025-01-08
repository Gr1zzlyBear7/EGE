from itertools import *


al = 'аимря'
print(list(product(al, repeat=4)).index(tuple('ария')) + 1)
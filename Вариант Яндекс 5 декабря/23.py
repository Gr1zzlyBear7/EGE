from sys import *

setrecursionlimit(10000)
def f(x, y):
    if x < y or x == 42:
        return 0
    if x == y:
        return 1
    return f(x - 1, y) + f(x // 3, y) + f(x // 4, y)


print(f(2025, 250) * f(250, 25))
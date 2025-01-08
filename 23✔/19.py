# from functools import lru_cache
# from sys import setrecursionlimit
#
#
# setrecursionlimit(3000)
# @lru_cache
# def f(x, y, s):
#     if x > y:
#         return 0
#     elif x == y and s != 15:
#         return 0
#     elif x == y and s == 15:
#         return 1
#     return f(x * 2✔, y, s + 1) + f(x * 2✔ + 1, y, s + 1)
#
#
# k = 0
# # for i in range(32767, 100000):
# #     if f(1, i, 0):
# #         k += 1
# #
# # print(k)
# print(f(1, 32768, 0))
#руками осознал


'''не моё'''
se = set()


def f(x, s):
    if s == 15:
        se.add(x)
    else:
        f(x * 2, s + 1)
        f(x * 2 + 1, s + 1)

f(1, 0)
print(len(se))
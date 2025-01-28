# a = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     b = 10 <= x <= 23
#     c = 12 <= x <= 30
#     f = not b or a or not c
#     if f_usl != f:
#         print(x)

x = 30
b = list(range(10, 22))
a = list(range(5, 18))
c = list(range(12, 31))
print((x not in b) and (x not in a) or (x in c))
x = 9
print((x not in b) and (x not in a) or (x in c))
x = 4
print((x not in b) and (x not in a) or (x in c))
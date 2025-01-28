def f(x, y, a):
    return (((x > 68) or (y > 89)) or ((2 * x - 7 * y) < a))


for a in range(130, 1000):
    if all([f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)]):
        print(a)
        break


# for a in range(-1000, 1000):
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if (((x > 68) or (y > 89)) or ((2 * x - 7 * y) < a)) == False:
#                 break
#         if (((x > 68) or (y > 89)) or ((2 * x - 7 * y) < a)) == False:
#             break
#     else:
#         print(a)
#         break
# # # # a = 0
# # # # f_usl = 1
# # # # for x in [k * 0.25 for k in range(-10000, 10000)]:
# # # #     b = 10 <= x <= 23
# # # #     c = 12 <= x <= 30
# # # #     f = not b or a or not c
# # # #     if f_usl != f:
# # # #         print(x)
# # #
# # # x = 30
# # # b = list(range(10, 22))
# # # a = list(range(5, 18))
# # # c = list(range(12, 31))
# # # print((x not in b) and (x not in a) or (x in c))
# # # x = 9
# # # print((x not in b) and (x not in a) or (x in c))
# # # x = 4
# # # print((x not in b) and (x not in a) or (x in c))
# #
# # a = 0
# # f_usl = 1
# # for x in [k * 0.25 for k in range(-10000, 10000)]:
# #     b = 10 <= x <= 21
# #     f = not b or a
# #     if f != f_usl:
# #         print(x)
#
# a = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 64 <= x <= 95
#     q = 72 <= x <= 106
#     f = ((q) and not a) <= ((not p) <= (not q))
#     if f != f_usl:
#         print(x)
#         print(106 - 95)

a = 0
f_usl = 1
for x in [k * 0.25 for k in range(-10000, 10000)]:
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    f = p <= ((q and not a) <= (not p))
    if f != f_usl:
        print(x)
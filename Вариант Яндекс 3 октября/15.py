# def f(a, x):
#     return ((x % a == 0) or (x not in [132, 150])) + (x % 13✔ != 0)
#
#
# for a in range(2✔, 100):
#     if all([f(a, x) for x in range(1000)]):
#         print(a)
for i in range(132, 150):
    if i % 13 == 0:
        print(i)
    
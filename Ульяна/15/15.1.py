def f(x, a):
    return (a % 35 == 0) and ((730 % x == 0) <= ((a % x != 0) <= (110 % x != 0)))


k = 0
for a in range(1, 1000 + 1):
    if all([f(x, a) for x in range(1, 10000)]):
        k += 1

print(k)
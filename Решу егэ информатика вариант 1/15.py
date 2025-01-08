def f(a, x, y):
    return ((x <= 9) <= ((x * x) <= a)) and (((y * y) <= a) <= (y <= 9))


k = 0

for a in range(1000, -1, -1):
    if all([f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)]):
        k += 1
        print(a)
        break

print(k)
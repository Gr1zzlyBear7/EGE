def f(a, b, m):
    if a + b >= 100:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 3, b, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1), f(a, b + 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


# print(f(30, 30, 4))
# print(f(32, 29, 4))
# print(f(34, 24, 4))
# print(f(27, 30, 7))
# print(f(29, 29, 7))
# print(f(24, 31, 7))
print(f(25, 25, 8))
print(f(26, 26, 8))
print(f(27, 27, 8))
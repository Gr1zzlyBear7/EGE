def f(a, b, m):
    if a + b <= 36:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a - 3, b, m - 1),
         f(a, b - 3, m - 1),
         f(a // 2 if a % 2 == 0 else a // 2 + 1, b, m - 1),
         f(a, b // 2 if b % 2 == 0 else b // 2 + 1, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(17, 1000) if f(20, s, 2)])
print([s for s in range(17, 1000) if not f(20, s, 1) and f(20, s, 3)])
print([s for s in range(17, 1000) if not f(20, s, 2) and f(20, s, 4)])

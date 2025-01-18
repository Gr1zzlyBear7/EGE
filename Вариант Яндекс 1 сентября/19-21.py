def f(a, b, m):
    if a + b >= 181:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 4, b, m - 1), f(a * 3, b, m - 1), f(a, b + 4, m - 1), f(a, b * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(1, 156) if f(25, s, 2)])
print([s for s in range(1, 156) if not f(25, s, 1) and f(25, s, 3)])
print([s for s in range(1, 156) if not f(25, s, 2) and f(25, s, 4)])

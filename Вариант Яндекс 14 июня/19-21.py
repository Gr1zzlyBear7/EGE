def f(a, m):
    if a >= 342:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 7, m - 1), f(a * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(1, 301) if f(s, 2)])
print([s for s in range(1, 301) if not f(s, 1) and f(s, 3)])
print([s for s in range(1, 301) if not f(s, 2) and f(s, 4)])
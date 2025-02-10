def f(a, b, m):
    if a + b >= 449:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 1, b, m - 1), f(a * 2, b, m - 1), f(a, b + 1, m - 1), f(a, b * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(1, 436) if f(11, s, 2)]) # all change to any, cause canclusion
print([s for s in range(1, 436) if not f(11, s, 1) and f(11, s, 3)])
print([s for s in range(1, 436) if not f(11, s, 2) and f(11, s, 4)])

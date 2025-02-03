def f(a, m, k):
    if a >= 29:
        return m % 2 == 0
    if m == 0:
        return 0
    h = []
    if k[-2] != 1:
        h += [f(a + 1, m - 1, k + [1])]
    if k[-2] != 2:
        h += [f(a + 2, m - 1, k + [2])]
    if k[-2] != 3:
        h += [f(a * 2, m - 1, k + [3])]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(1, 29) if not f(s, 1, [0, 0]) and f(s, 3, [0, 0])])
print([s for s in range(1, 29) if not f(s, 2, [0, 0]) and f(s, 4, [0, 0])])
print([s for s in range(1, 29) if not f(s, 1, [0, 0]) and not f(s, 3, [0, 0]) and f(s, 5, [0, 0])])




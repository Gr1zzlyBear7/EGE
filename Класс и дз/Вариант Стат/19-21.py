def f(a, m):
    if a <= 9:
        return m % 2 == 0
    if m == 0:
        return 0
    k = [x for x in range(2, 10)]
    h = []
    for x in k:
        if a % x == 0:
            h.append(f(a - x, m - 1))
    if not h:
        h = [f(a - 1, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(10, 1000) if f(s, 2)])
print([s for s in range(10, 1000) if not f(s, 1) and f(s, 3)])
print([s for s in range(10, 1000) if not f(s, 2) and f(s, 4)])


def f(a, b, m):
    if a + b >= 189:
        return m % 2 == 0
    if m == 0:
        return 0
    if a <= b:
        h = [f(a + b, b, m - 1), f(a + (b - a), b, m - 1), f(a, b + a, m - 1)]
    else:
        h = [f(a + b, b, m - 1), f(a, b + (a - b), m - 1), f(a, b + a, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(1, 184) if f(5, s, 2)]) # all меняем на any т.к. условие после неудачного хода
print([s for s in range(1, 184) if not f(5, s, 1) and f(5, s, 3)])
print([s for s in range(1, 184) if not f(5, s, 2) and f(5, s, 4)])


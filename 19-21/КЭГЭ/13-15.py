def f(a, b, m):
    if a + b >= 68:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 1, b, m - 1), f(a + b, b, m - 1), f(a, b + 1, m - 1), f(a, b + a, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(1, 60) if f(8, s, 2)])  # all меняем на any, т.к. условие после неудачного хода, получаем 18
print([s for s in range(1, 60) if not f(8, s, 1) and f(8, s, 3)])
print([s for s in range(1, 60) if not f(8, s, 2) and f(8, s, 4)])

def f(a, b, m):
    if a + b <= 33:
        return m % 2 == 0
    if m == 0:
        return 0
    if a > b:
        if a % 2 == 0:
            h = [f(a - 2, b, m - 1), f(a // 2, b, m - 1), f(a, b - 2, m - 1)]
        else:
            h = [f(a - 2, b, m - 1), f(a // 2 + 1, b, m - 1), f(a, b - 2, m - 1)]
    else:
        if b % 2 == 0:
            h = [f(a - 2, b, m - 1), f(a, b // 2, m - 1), f(a, b - 2, m - 1)]
        else:
            h = [f(a - 2, b, m - 1), f(a, b // 2 + 1, m - 1), f(a, b - 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(11, 200) if f(23, s, 2)]) # all меняем на any т.к. после неудачного хода
print([s for s in range(11, 200) if not f(23, s, 1) and f(23, s, 3)])
print([s for s in range(11, 200) if not f(23, s, 2) and f(23, s, 4)])


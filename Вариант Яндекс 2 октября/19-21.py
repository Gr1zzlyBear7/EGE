def f(a, b, m):
    if a + b >= 231:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 4, b, m - 1), f(a * 3, b, m - 1), f(a, b + 4, m - 1), f(a, b * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(1, 218) if f(10, s, 2)]) # all меняем на any, т.к. условие неудачный ход
print([s for s in range(1, 218) if not f(10, s, 1) and f(10, s, 3)])
print([s for s in range(1, 218) if not f(10, s, 2) and f(10, s, 4)])



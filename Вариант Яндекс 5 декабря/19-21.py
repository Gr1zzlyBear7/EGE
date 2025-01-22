def f(a, b, m, choco):
    if a + b <= 42:
        return m % 2 == 0
    if m == 0:
        return 0
    if choco == 0:
        h = [f(a - 4, b, m - 1, 'a4'), f(a // 3, b, m - 1, 'a3'),
             f(a, b - 4, m - 1, 'b4'), f(a, b // 3, m - 1, 'b3')]
    elif choco == 'a4':
        h = [f(a // 3, b, m - 1, 'a3'),
             f(a, b - 4, m - 1, 'b4'), f(a, b // 3, m - 1, 'b3')]
    elif choco == 'a3':
        h = [f(a - 4, b, m - 1, 'a4'),
             f(a, b - 4, m - 1, 'b4'), f(a, b // 3, m - 1, 'b3')]
    elif choco == 'b4':
        h = [f(a - 4, b, m - 1, 'a4'), f(a // 3, b, m - 1, 'a3'),
             f(a, b // 3, m - 1, 'b3')]
    else:
        h = [f(a - 4, b, m - 1, 'a4'), f(a // 3, b, m - 1, 'a3'),
             f(a, b - 4, m - 1, 'b4')]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print([s for s in range(2, 100) if f(50, s, 2, 0)])
print([s for s in range(2, 100) if not f(50, s, 1, 0) and f(50, s, 3, 0)])
print([s for s in range(2, 100) if not f(50, s, 2, 0) and f(50, s, 4, 0)])

def divs(n):
    div = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            div.append(i)
            if n // i != i:
                div.append(n // i)
    return sum(div)


def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + divs(x), y)


print(f(2, 62))
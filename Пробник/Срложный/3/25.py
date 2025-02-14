def f(n):
    div = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2:
                if i in arr:
                    div.append(i)
            if n // i != i:
                if (n // i) % 2:
                    if n // i in arr:
                        div.append(n // i)
    return div


arr = set([x ** 3 for x in range(3, 100, 2)])
for i in range(228224, 531135 + 1):
    if len(f(i)) >= 4:
        print(len(f(i)), max(f(i)))



def f(n):
    if n <= 1:
        return 1/2
    return (n + 1) * f(n - 1)


print(f(200) / f(198))
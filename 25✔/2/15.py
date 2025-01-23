def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def div(n):
    s = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i) and i != n:
                s += i
            if (n // i) != i and n // i != n:
                if is_prime((n // i)):
                    s += (n // i)
    return s


k = 0
for i in range(500_000, -1, -1):
    if div(i) % 10 == 0 and div(i) != 0:
        print(i, div(i))
        k += 1
    if k == 7:
        break
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def div(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                divs.append(i)
            if (n // i) != i:
                if is_prime((n // i)):
                    divs.append((n // i))
    return len(divs) >= 6, max(divs) if len(divs) >= 6 else 0


for i in range(25317, 51238):
    if div(i)[0]:
        print(i, div(i)[1])
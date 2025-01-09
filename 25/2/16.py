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
    return len(divs) == 2, divs


for i in range(125697, 125722):
    if div(i)[0]:
        arr = div(i)[1]
        if arr[0] * arr[1] == i:
            print(*arr)
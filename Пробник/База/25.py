def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def divs(n):
    div = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                div.append(i)
            if n // i != i:
                if is_prime(n // i):
                    div.append(n // i)
    if div:
        return max(div) + min(div)
    return 0


k = 0
for i in range(1_200_000, 10 ** 100):
    const = divs(i)
    if const > 2000 and const % 10 == 8:
        print(i, const)
        k += 1
    if k == 5:
        break
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
            if (n // i) != i:
                if is_prime((n // i)):
                    div.append((n // i))
    if div and len(div) == 3 and div[0] * div[1] * div[2] == n:
        return max(div) - min(div) <= 12, max(div) - min(div)
    return False, False


for i in range(326782, 965324 + 1):
    if divs(i)[0]:
        print(i, divs(i)[1])
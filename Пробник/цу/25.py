def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def divs(n):
    div = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            div.append(i)
            if n // i != i:
                div.append(n // i)
    div.sort()
    if len(div) < 3:
        return 0
    return div[0] + div[-1] + div[-2]


print(is_prime(divs(1000000001)))
k = 0
ans = []
for n in range(10 ** 9 + 1, 10 ** 10):
    const = divs(n)
    if is_prime(const):
        ans.append(str(n))
        k += 1
    if k == 5:
        break
print(' '.join(ans))
def divs(n):
    div = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            div.append(i)
            if n // i != i:
                div.append(n // i)
    if div:
        return len(set(div)) == 6, max(div) + min(div)
    return False, 0


k = 0
for i in range(650_000, 10 ** 1000):
    const = divs(i)
    if const[0]:
        if len(str(const[1])) == 4:
            k += 1
            print(i, const[1])
    if k == 5:
        break
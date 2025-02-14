def div(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if n // i != i:
                divs.append(n // i)
    return len(divs) == 3


for i in range(1, 1000):
    s = '>' + 15 * '1' + 35 * '2' + i * '3'
    while '>1' in s or '>2' in s or '>3' in s:
        s = s.replace('>1', '2>', 1)
        s = s.replace('>2', '3>', 1)
        s = s.replace('>3', '11>', 1)
    if div(sum(map(int, s[:-1]))):
        print(i)
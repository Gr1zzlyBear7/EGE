def five(n):
    new = ''
    while n > 0:
        new += str(n % 5)
        n //= 5
    return new[::-1]


def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


data = list(map(int, open('17')))
ans = []
for elem in data:
    if tri(elem)[-1] == five(elem)[-1]:
        if elem % 31 == 0 or elem % 47 == 0 or elem % 53 == 0:
            ans.append(elem)
print(len(ans), min(ans))
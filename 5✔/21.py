ans = []

for n in range(1, 10000000):
    num = n
    if n % 3 == 0:
        num //= 3
    else:
        num -= 1
    if num % 5 == 0:
        num //= 5
    else:
        num -= 1
    if num % 11 == 0:
        num //= 11
    else:
        num -= 1
    if num == 8:
        ans.append(n)

print(len(ans))
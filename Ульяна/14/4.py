def seven(n):
    new = ''
    while n > 0:
        new += str(n % 7)
        n //= 7
    return new


arr = []
const = 7 ** 400 + 7 ** 300
for x in range(7 ** 400, 7 ** 399, -1):
    arr.append(seven(const - x).count('0'))
    print(max(arr))
print(max(arr))
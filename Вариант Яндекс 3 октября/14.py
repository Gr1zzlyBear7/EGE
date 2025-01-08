def nine(n):
    new = ''
    while n > 0:
        new += str(n % 9)
        n //= 9
    return (new[::-1])


arr = []
const = 72070 + 7400
for x in range(1950, -1, -1):
    arr.append(nine(const - x).count('0'))
print(max(arr))
def f(n):
    new = ''
    while n > 0:
        new += str(n % 4)
        n //= 4
    return new


const = 4 ** 210 + 4 ** 110
ans = []
for x in range(0, 3000):
    if f(const - x).count('0') == 105:
        print(x)
        print(f(const - x))
        break
    # ans.append(f(const - x).count('0'))
# print(max(ans))
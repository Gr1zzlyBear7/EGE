def is_prime(n):
    if n <= 1:
        return False
    for z in range(2, int(n ** 0.5) + 1):
        if n % z == 0:
            return False
    return True


data = list(map(int, open('UZY_Q-7K9.txt')))
ans = []
ma = max([x for x in data if abs(x) % 100 == 17])
for i in range(len(data) - 1):
    dva = [*data[i:i + 2]]
    c1 = [x for x in dva if is_prime((x))]
    if len(c1) == 1:
        if abs(sum(dva)) % ma == 0:
            print(dva)
            ans.append(dva[0] * dva[1])
print(len(ans), max(ans))
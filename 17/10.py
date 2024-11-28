def three(num):
    new = ''
    while num > 0:
        new += str(num % 3)
        num //= 3
    return int(new[::-1])


with open('10.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [min(data[i], data[i + 1], data[i + 2]) for i in range(len(data) - 2) if
           (three(data[i]) % 10 == 2 or three(data[i + 1]) % 10 == 2 or three(data[i + 2]) % 10 == 2)]
    print(len(ans), sum(ans))

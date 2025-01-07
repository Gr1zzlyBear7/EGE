with open('9.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [(data[i] + data[i + 1] + data[i + 2]) / 3 for i in range(len(data) - 2) if
           (abs(data[i]) % 12 == 0 or abs(data[i + 1]) % 12 == 0 or abs(data[i + 2]) % 12 == 0) and abs(
               data[i]) % 3 == 0 and abs(data[i + 1]) % 3 == 0 and abs(data[i + 2]) % 3 == 0]
    print(len(ans), min(ans))

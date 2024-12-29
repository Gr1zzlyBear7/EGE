with open('8.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [data[i] + data[i + 1] + data[i + 2] for i in range(len(data) - 2) if
           abs(data[i] * data[i + 1] * data[i + 2]) % 7 == 0 and abs(data[i] + data[i + 1] + data[i + 2]) % 10 == 5]
    print(len(ans), max(ans))

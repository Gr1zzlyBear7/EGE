with open('7.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [data[i] * data[i + 1] for i in range(len(data) - 1) if (data[i] * data[i + 1] > 0 and abs(data[i] + data[i + 1]) % 7 == 0)]
    print(len(ans), min(ans))
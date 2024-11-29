with open('11.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [data[i] + data[i + 1] + data[i + 2] + data[i + 3] for i in range(len(data) - 3) if
           data[i] > data[i + 1] > data[i + 2] > data[i + 3] and data[i] - data[i + 3] > 1000]
    print(len(ans), min(ans))

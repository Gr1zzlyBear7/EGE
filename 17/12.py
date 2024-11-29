with open('12.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [data[i] * data[i + 1] for i in range(len(data) - 1) if
           data[i] + data[i + 1] >= 100 and (data[i] < 0 or data[i + 1] < 0)]
    print(len(ans), max(ans))

data = list(map(int, open('17').readlines()))

ans = []
for i in range(2, len(data) - 3):
    if data[i] + data[i + 1] > data[i - 1] + data[i - 2] >= 0 and data[i] + data[i + 1] > data[i + 2] + data[i + 3] >= 0:
        ans.append(data[i] * data[i + 1])
        print(data[i] + data[i + 1], data[i - 1] + data[i - 2])
        print(data[i] + data[i + 1], data[i + 2] + data[i + 3])
print(len(ans), min(ans))
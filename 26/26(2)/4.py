data = list(map(int, open('4')))
data.sort()

conclusion_1 = 5000 // 2
conclusion_2 = 5000 // 4

ans = []

for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if (data[i] + data[j]) % 2 == 0:
            sr = (data[i] + data[j]) // 2
            if sr < data[5000 - conclusion_2]:
                if sr > data[5000 - 2500 - 1]:
                    ans.append(sr)
print(len(ans), min(ans))

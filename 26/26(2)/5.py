data = list(map(int, open('5')))
set_data = set(data)
ans = []
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if data[i] % 2 == 0 and data[j] % 2 != 0 or \
                data[j] % 2 == 0 and data[i] % 2 != 0:
            if (data[i] + data[j]) in set_data:
                ans.append(data[i] + data[j])
print(len(ans), max(ans))

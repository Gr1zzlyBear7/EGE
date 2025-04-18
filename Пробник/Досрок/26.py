data = sorted([int(x) for x in open('26.txt')], reverse=True)
print(data)
k = 1
m = data[0]
for x in range(len(data) - 1):
    if m - data[x + 1] >= 9:
        k += 1
        m = data[x + 1]
        print(data[x + 1])
print(k)
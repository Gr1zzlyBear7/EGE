m = 820
data = list(map(int, open('5')))
need = int(sum(data) / len(data)) + 1
data.sort()
clever = list(filter(lambda x: x >= need, data))
clever.sort(reverse=True)
elephants = list(set(clever[:m]))
clever_soso = clever[m:]
if elephants[0] in clever_soso:
    print(elephants[1], elephants[0])
else:
    print(elephants[0])
others = data[:data.index(elephants[0])]

print(int(sum(others) / len(others)))
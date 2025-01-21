data = list(map(int, open('6')))
print(len(set(data)), data.count(sorted(data, key=data.count)[-1]))

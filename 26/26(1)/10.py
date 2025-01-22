data = list(map(int, open('10')))
data.sort(reverse=True)
slice = (int(10000 * 0.2))
new = data[:slice]
other = data[slice:]
diff = []
k = 0
for i in range(0, len(other) - 1):
    diff.append(other[i] - other[i + 1])

print(diff.index(max(diff)) + 1 + len(new), end=' ')
print(other[diff.index(max(diff))])
s = 99987
data = list(map(int, open('4')))
data.sort()
arr = []
while sum(arr) + data[0] <= s:
    arr.append(data.pop(0))
print(len(data), sum(data))
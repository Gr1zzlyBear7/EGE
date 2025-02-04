
k = 47
s = 1263519
m = 51
data = [list(map(int, x.split())) for x in open('26.txt')]
my_types = {x[0]: [] for x in data}
for t, v in data:
    my_types[t].append(v)
    my_types[t].sort()
total = 0
for t in my_types:
    arr = my_types[t]
    i = 0
    while i < m:
        total += 1
        s -= arr[0]
        arr.pop(0)
        i += 1
ma = 0
const = []
for t in my_types:
    total_s = s
    k = m
    useless = [0]
    arr = my_types[t]
    if arr:
        while sum(useless) + arr[0] <= total_s:
            k += 1
            useless.append(arr.pop(0))
            if not arr:
                break
        const.append(k)
print(total - m + max(const), max(const))
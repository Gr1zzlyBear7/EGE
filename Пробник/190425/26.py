data = [list(map(int, x.split())) for x in open('26.txt')]

ids = {x: [[], 0] for x, y in data}
for id, v in data:
    if v not in ids[id][0]:
        ids[id][0].append(v)
    ids[id][0].sort()
for id, tusks in list(ids.items()):
    arr = tusks[0]
    k = 1
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == 2:
            k += 1
        else:
            ids[id][1] = max(ids[id][1], k)
            k = 1
    ids[id][1] = max(ids[id][1], k)
ans = [[x[0], x[1][1]] for x in list(ids.items())]
ans.sort(key=lambda x: (-x[1], x[0]))
for x in ans:
    print(x)
s = 600
data = list(map(int, open('3')))
data.sort(reverse=True)
ans = [0] * 1000
k = 0
while True:
    to_del = []
    for i in range(len(data)):
        if ans[k] + data[i] <= s:
            ans[k] += data[i]
            to_del.append(data[i])
    while to_del:
        data.remove(to_del[0])
        to_del.pop(0)
    k += 1
    if k == 1000:
        break
ans = [x for x in ans if x != 0]
print(len(ans), ans[-1])

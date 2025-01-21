data = list(map(int, open('3.txt')))
mem = 524288
half_mem = mem // 2
data.sort()
arr = []
vid = list(filter(lambda x: x >= 101, data))
pho = list(filter(lambda x: x <= 100, data))
while sum(arr) <= half_mem:
    arr.append(vid.pop(0))
while sum(arr) + pho[0] <= mem:
    arr.append(pho.pop(0))
for i in range(len(pho)):
    if sum(arr) - arr[-1] + pho[i] <= mem:
        arr[-1], pho[i] = pho[i], arr[-1]

print(mem - sum(arr), len(arr))

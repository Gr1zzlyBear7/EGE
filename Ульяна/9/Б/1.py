data = [list(map(int, x.split())) for x in open('1')]
k = 0
for line in data:
    arr = line
    arr.sort()
    new = [arr.pop(0), arr.pop()]
    if sum(new) <= sum(arr):
        k += 1
print(k)
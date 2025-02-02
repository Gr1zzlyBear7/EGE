from copy import deepcopy
m = 100
data = [list(map(int, x.split())) for x in open('26.txt')]
four = list(filter(lambda x: len(x) == 5, data))
arr = deepcopy(data)
for x in four:
    arr.remove(x)
new = []
for x in four:
    maxi = max(x[-1], x[-2])
    new.append([*x[:3], maxi])
tot = arr + new
tot.sort(key=lambda x: (-x[0], -sum(x[1:])))
for i in tot:
    print(i[0], sum(i[1:]))
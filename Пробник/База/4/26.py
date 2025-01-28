from copy import deepcopy
data = list(map(int, open('26.txt')))
data.sort()
print(data)
need = len(data) / 3
print(need)
data_c = deepcopy(data)
total = 0
for i in range(int(need)):
    new = [data.pop(0), data.pop(0), data.pop()]
    total += new[-1]
ans_1 = (sum(data_c) - total)
data = list(map(int, open('26.txt')))
data.sort()
total = 0
for i in range(int(need)):
    new = [data.pop(), data.pop(), data.pop()]
    total += min(new)
print(ans_1, sum(data_c) - total)
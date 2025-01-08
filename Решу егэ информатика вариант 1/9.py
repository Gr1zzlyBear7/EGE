data = [list(map(int, line.split())) for line in open('9').readlines()]

data_all = [x for line in data for x in line]

k = 0

for line in data:
    for x in line:
        if line.count(x) == 1:
            if data_all.count(x) == 46:
                k += 1
                break
print(k)

k = 0

for line in data:
    if any([line.count(n) == 1 and data_all.count(n) == 46 for n in line]):
        k += 1

print(k)

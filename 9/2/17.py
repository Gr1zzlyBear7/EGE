data = [list(map(int, line.split())) for line in open('17')]
k = 0
for line in data:
    arr = [line.count(x) for x in set(line)]
    if 1 in arr and len(arr) < 6:
        arr_1 = [x for x in line if line.count(x) == 1]
        arr_2 = [x for x in line if line.count(x) > 1]
        sr_1 = 0 if len(arr_1) == 0 else sum(arr_1) / len(arr_1)
        sr_2 = 0 if len(arr_2) == 0 else sum(arr_2) / len(arr_2)
        if sr_1 < sr_2:
            k += 1


print(k)
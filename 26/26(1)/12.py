data = [list(map(int, x.split())) for x in open('12')]
rows = [x[0] for x in data]
rows = list(set(rows))
rows.sort(reverse=True)

my_rows = {}
for row in rows:
    my_rows[row] = [[], 0]
for row, seat in data:
    my_rows[row][0].append(seat)
for row in my_rows:
    my_rows[row][0].sort()
maxes = []
print(my_rows)
for row in my_rows:
    maxi = k = 0
    arr = my_rows[row][0]
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1] - 1:
            k += 1
        else:
            maxi = max(maxi, k)
            k = 1
    maxi = max(maxi, k)
    my_rows[row][1] = maxi
    maxes.append(maxi)
ind = maxes.index(max(maxes))
k = 0
for row in my_rows:
    if k == ind:
        print(row, my_rows[row][1])
        break
    k += 1
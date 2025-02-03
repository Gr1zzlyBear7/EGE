data = [list(map(int, x.split())) for x in open('26.txt')]
my_rows = {x[0]: [] for x in data}
for r, s in data:
    my_rows[r].append(s)
    my_rows[r].sort()
total = 0
for row in my_rows:
    arr = my_rows[row]
    for i in range(1, len(arr) - 1):
        if arr[i] - arr[i - 1] == arr[i + 1] - arr[i] == 6:
            total += 1
            print(row)
print(total)
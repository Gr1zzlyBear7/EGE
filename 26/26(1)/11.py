data = [list(map(int, x.split())) for x in open('11')]
rows = list(set([x[0] for x in data]))
rows.sort(reverse=True)
my_rows = {}
for row in rows:
    my_rows[row] = []
for row, seat in data:
    my_rows[row].append(seat)
for row in my_rows:
    my_rows[row].sort()
for row in my_rows:
    const = len(my_rows[row])
    flag = False
    if const >= 2:
        for i in range(const - 1):
            if my_rows[row][i + 1] - my_rows[row][i] == 3:
                print(row, my_rows[row][i] + 1)
                flag = True
                break
        else:
            flag = False
    if flag:
        break
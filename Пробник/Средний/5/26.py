data = [list(map(int, x.split())) for x in open('26.txt')]
my_rows = {x[0]: [] for x in data}
my_rows = list(my_rows.keys())
my_rows = {x: [] for x in sorted(my_rows, reverse=True)}
for r, s in data:
    my_rows[r].append(s)
    my_rows[r].sort()
print(my_rows)

data = [list(map(int, line.split())) for line in open('9')]
k = 0
ans = []
for line in data:
    my_set = set(line)
    arr = [x for x in line if abs(x) % 2 == 1]
    if len(my_set) < 4 and len(arr) != 3:
        k += 1
    elif len(my_set) == 4 and len(arr) == 3:
        k += 1

print(k)
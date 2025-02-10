data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
new = [[122, 122, 127, 140, 140], [81, 81, 135, 137, 137]]

for line in new:
    c1 = [line.count(x) for x in set(line)]
    if c1.count(2) == 2 and len(c1) == 3:
        arr = sorted(line, key=line.count)
        print(arr)
        k += 1
print(k)
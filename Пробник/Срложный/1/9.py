data = [list(map(int, x.split())) for x in open('9.txt')]
total = []
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if len(c1) == 3 and c1.count(2) == 2 and c1.count(3) == 1:
        arr = sorted(line)[:4]
        ev = [x for x in arr if x % 2 == 0]
        if len(ev) == 2:
            total.append(sum(line))
print(sum(total))
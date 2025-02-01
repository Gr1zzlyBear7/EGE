data = [list(map(int, x.split())) for x in open('5')]
k = 1
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if c1.count(3) == 2 and len(c1) == 4:
        if line.count(min(line)) == 1:
            print(sum(line))
            break
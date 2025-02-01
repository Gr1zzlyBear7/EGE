data = [list(map(int, x.split())) for x in open('7')]
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if c1.count(2) == 2 and len(c1) == 5:
        if line.count(max(line)) == 1:
            print(sum(line))
            break
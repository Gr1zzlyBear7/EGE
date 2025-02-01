data = [list(map(int, x.split())) for x in open('1')]
k = 1
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if len(c1) == 5 and 3 in c1:
        evens = [x for x in line if x % 2 == 0]
        odds = [x for x in line if x % 2 == 1]
        if len(evens) > len(odds):
            print(k)
    k += 1


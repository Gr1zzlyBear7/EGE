data = [list(map(int, x.split())) for x in open('2')]
k = 0
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if len(c1) == 5 and 2 in c1:
        evens = [x for x in line if x % 2 == 0]
        odds = [x for x in line if x % 2 == 1]
        sr1 = sum(evens) / len(evens) if len(evens) != 0 else 0
        sr2 = sum(odds) / len(odds) if len(odds) != 0 else 0
        if abs(sr1 - sr2) > 50:
            pass
        else:
            k += 1
    else:
        evens = [x for x in line if x % 2 == 0]
        odds = [x for x in line if x % 2 == 1]
        sr1 = sum(evens) / len(evens) if len(evens) != 0 else 0
        sr2 = sum(odds) / len(odds) if len(odds) != 0 else 0
        if abs(sr1 - sr2) > 50:
            k += 1
print(k)
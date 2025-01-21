data = [list(map(int, x.split())) for x in open('9')]
k = 0
for line in data:
    odds = [x for x in line if x % 2 == 1]
    evens = [x for x in line if x % 2 == 0]
    if len(odds) >= 2 and len(evens) >= 2:
        s = 1
        for i in evens:
            s *= i
        if sum(odds) * 3 > s:
            k += 1
print(k)
data = [list(map(int, x.split())) for x in open('26.txt')]
arr = [x for x in data if 2 not in x]
dva = [x for x in data if 2 in x]
arr.sort(key=lambda x: (-sum(x[1:]), x[0]))
c1 = (9964 * 0.25)
c = 0
for x in arr:
    if 2 not in x:
        print(x)
        c += 1
    if c == c1:
        break
dva.sort(key=lambda x: (x[1:].count(2), x[0]))
for x in dva:
    if x.count(2) > 2:
        print(x)
        break
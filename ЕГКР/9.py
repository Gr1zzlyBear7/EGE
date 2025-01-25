data = [list(map(int, x.split())) for x in open('9')]
k = 0
ans = []
for line in data:
    arr = [line.count(x) for x in set(line)]
    if arr.count(3) == 2 and arr.count(1) == 1:
        new = sorted([x for x in line], key=line.count)
        one = new[0]
        more = new[1:]
        if one > sum(more) / len(more):
            k += 1
            print(new, sum(more) / len(more))
print(k)
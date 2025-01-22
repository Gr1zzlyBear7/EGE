data = [list(map(int, x.split())) for x in open('9')]
k = 0
ans = []
for line in data:
    if sum(sorted(line)[1:-1]) / 3 >= 8:
        k += 1
print(k)

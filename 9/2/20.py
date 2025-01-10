data = [list(map(int, line.split())) for line in open('20')]
k = 0
for line in data:
    arr = [x for x in line if x % 3 == 0]
    if len(arr) == 3:
        if max(line) - min(line) <= sum(arr):
            k += 1

print(k)
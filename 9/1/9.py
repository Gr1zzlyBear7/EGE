data = [list(map(int, line.split())) for line in open('9')]

k = 0
for line in data:
    if sum(line) == 180:
        k += 1
print(k)
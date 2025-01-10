data = [list(map(int, line.split())) for line in open('8')]

k = 0
for line in data:
    if len(set(line)) == 2:
        k += 1

print(k)
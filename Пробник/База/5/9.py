data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    if (line[1] + line[0]) / 2 == line[2]:
        k += 1
print(k)
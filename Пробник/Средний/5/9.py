data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    if len(set(line)) == 4:
        k += 1
print(k)
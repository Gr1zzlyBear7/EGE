data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    c1 = [x for x in line if x < 0]
    c2 = [x for x in line if x > 0]
    if len(c1) and len(c2) and len(c1) > len(c2):
        if abs(min(line)) > max(line):
            k += 1
print(k)
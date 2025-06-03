data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    c1 = [x for x in line if x < 0]
    if 3 <= len(c1) <= 4:
        if abs(min(line)) > max(line):
            k += 1
            print(line)
print(k)
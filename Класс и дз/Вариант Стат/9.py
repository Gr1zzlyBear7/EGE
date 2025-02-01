data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    if line.count(max(line)) == 1:
        if max(line) in line[:4]:
            first = line[:4]
            second = line[4:]
            if sum(first) / len(first) < sum(second) / len(second):
                k += 1
print(k)
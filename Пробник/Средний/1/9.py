data = [list(map(int, x.split())) for x in open('9')]
k = 0
for line in data:
    if len(set(line)) == len(line):
        if (max(line) + min(line)) * 3 >= (sum(line) - max(line) - min(line)) * 2:
            k += 1
            print(line)
print(k)

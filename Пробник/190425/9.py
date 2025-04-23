data = [list(map(int, x.split())) for x in open('9.txt')]
k = 1
for line in data:
    if sorted(line, reverse=True) == line:
        if (max(line) + min(line)) / 2 > (sum(line) - max(line) + min(line)) / 5:
            print(sum(line))
            print(k)
            break
    k += 1
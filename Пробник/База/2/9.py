data = [list(map(int, x.split())) for x in open('9')]
k = 0
for line in data:
    if max(line) - min(line) >= 50:
        # s = 1
        # for x in line:
        #     s *= x
        # s /= max(line)
        # s /= min(line)
        # if s <= 1000:
        #     k += 1
        new = sorted(line)
        new = new[1:3]
        s = 1
        for x in new:
            s *= x
        if s <= 1000:
            k += 1
print(k)
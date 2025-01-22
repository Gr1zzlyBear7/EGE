data = [list(map(int, x.split())) for x in open('9')]
pie = 0
ans = []
for line in data:
    choco = 0
    arr = [line.count(x) for x in line]
    evens = [x for x in line if x % 2 == 0]
    odds = [x for x in line if x % 2 == 1]
    giga_choco_pie = sorted(line)[-2:]
    normis_choco_pie = sorted(line)[:-2]
    if 3 in arr and len(set(line)) == 4:
        choco += 1
    if len(evens) > len(odds):
        choco += 1
    if sum(giga_choco_pie) > sum(normis_choco_pie) * 2:
        choco += 1
    if choco >= 2:
        pie += 1
print(pie)

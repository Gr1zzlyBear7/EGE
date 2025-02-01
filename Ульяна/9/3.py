data = [list(map(int, x.split())) for x in open('3')]
nums = []
k = 1
for line in data:
    if len(set(line)) == len(line):
        new = line
        new.sort()
        sq = [new.pop(0), new.pop()]
        if sum(sq) ** 2 > new[0] * new[1] * new[2]:
            nums.append(k)
    k += 1
print(sum(nums))
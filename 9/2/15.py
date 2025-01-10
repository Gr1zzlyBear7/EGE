data = [list(map(int, line.split())) for line in open('15')]
k = 0
for line in data:
    arr = [line.count(x) for x in set(line)]
    if len(arr) == 5 and arr.count(2) == 2:
        if line.count(max(line)) == 1:
            print(sum(line))
            break
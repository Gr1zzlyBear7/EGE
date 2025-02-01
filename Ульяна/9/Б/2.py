data = [list(map(int, x.split())) for x in open('2')]
k = 0
for line in data:
    arr = sorted(line)
    maxi = arr.pop()
    if sum(arr) > maxi:
        if len(set(line)) == 3:
            k += 1
print(k)
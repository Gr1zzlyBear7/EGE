data = [list(map(int, x.split())) for x in open('4')]
k = 0
for line in data:
    arr = sorted(line)
    maxi = arr.pop()
    if maxi ** 2 > 2 * arr[0] * arr[1]:
        k += 1
print(k)
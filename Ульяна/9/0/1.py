data = [list(map(int, x.split())) for x in open('1')]
k = 0
for line in data:
    a, b, c = line[0], line[1], line[2]
    if a + b > c and a + c > b and c + b > a:
        k += 1
print(k)

from collections import Counter
data = [list(map(int, x.split()[1:2])) for x in open('26')]
new = []
for x in data:
    new += x
maxi = Counter(new).most_common()[0][1]
my_d = {}
for x in new:
    if x not in my_d:
        my_d[x] = 1
    else:
        my_d[x] += 1
    if my_d[x] == 15:
        print(x)
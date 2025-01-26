s = 500
data = [list(map(int, x.split())) for x in open('26')]
product = list(set([x[0] for x in data]))
product.sort()
my_product = {}
for p in product:
    my_product[p] = []
for p, t in data:
    my_product[p].append(t)
for p in my_product:
    my_product[p].sort()
for p in my_product:
    arr = my_product[p]
    total = []
    while True:
        if sum(total) + arr[0] <= s:
            total.append(arr.pop(0))
        else:
            break
        if len(arr) == 0:
            break
total = 0
for p in my_product:
    total += len(my_product[p])
new = [[x, y] for x, y in my_product.items()]
new.sort(key=lambda x: (-len(x[1]), -x[0]))
for x in new:
    print(total, x[0])
    break
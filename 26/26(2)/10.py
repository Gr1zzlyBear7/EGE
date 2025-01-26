f = open('10')
a = list(map(int, f))
a.sort()
weight = [0] * (sum(a) + 1)

for i in range(150):
    weight2 = weight.copy()
    for j in range(len(weight)):
        if weight[j] > 0:
            weight2[j + a[i]] += weight[j]
    weight2[a[i]] += 1
    weight = weight2
weight = ''.join([str(x) for x in weight])
weight = weight[:(weight.rfind('1'))]
print(weight.count('0'))
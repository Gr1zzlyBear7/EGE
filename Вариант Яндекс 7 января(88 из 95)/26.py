L = 724
P = 813
data = [list(map(int, x.split())) for x in open('26')]
lots_cost = [[x[0], x[2]] for x in data]
lots = [x[0] for x in data]
print(lots_cost)
my_lots = {}
for i in range(0, L + 1):
    my_lots[i] = [0, []]
z = 0
for number, cost in lots_cost:
    if z == 63:
        pass
    my_lots[number][0] += 1
    my_lots[number][1].append(cost)
    z += 1
total = 0
count = 0
for k in my_lots:
    if my_lots[k][0] >= 2:
        total += sorted(my_lots[k][1])[-2]
        count += 1
print(count, total)
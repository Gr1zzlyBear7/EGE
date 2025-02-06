data = [list(map(int, x.split())) for x in open('26.txt')]
t = 10000000
level = [x[0] for x in data]
sr = sum(level) / len(level)
super_vir = list(filter(lambda x: x > sr, level))

vir = [[x[0], x[1]] for x in data if x[0] not in super_vir]
vir.sort(key=lambda x: x[1])

super_vir = [[x[0], x[1]] for x in data if x[0] in super_vir]
super_vir.sort(key=lambda x: x[1])
total = [[], []]
"""
РЕШЕНИЕ НА 1 БАЛЛ
while True:
    if t < sum(total[0]) + super_vir[0][1] + sum(total[1]):
        break
    total[0].append(super_vir.pop(0)[1])
    if vir:
        if t < sum(total[1]) + vir[0][1] + sum(total[0]):
            total[0].pop()
            break
    else:
        total[0].pop()
        break
    total[1].append(vir.pop(0)[1])
print(len(total[0]) + len(total[1]), sum(total[0]), )
"""
k, sall, sp = 0, 0, 0
for i in range(len(vir)):
    if i < len(super_vir) and sall + vir[i][1] + super_vir[i][1] <= t:
        sall += vir[i][1] + super_vir[i][1]
        sp += super_vir[i][1]
        k += 2
    elif sall + vir[i][1] <= t:
        sall += vir[i][1]
        k += 1
print(k, sp)


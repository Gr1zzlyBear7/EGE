data = [list(map(int, x.split())) for x in open('26.txt')]
places = 9964 * 0.25
need1 = list(filter(lambda x: x.count(2) == 0, data))
need1 = sorted(need1, key=lambda x: (-sum(x[1:]), x[0]))


ans1 = need1[:int(places)]
# for i in ans1:
#     print(i)
need = list(filter(lambda x: x.count(2) >= 2, data))
ans2 = sorted(need, key=lambda x: (-(x.count(2) == 3), x[0]))
for i in ans2:
    print(i)
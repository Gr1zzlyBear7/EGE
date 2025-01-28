data = [list(map(int, x.split())) for x in open('26')]
my_id = {x[0]: [x[1:], [], [], []] for x in data}

for id in my_id:
    arr = my_id[id][0]
    my_id[id][1].append(sum(arr))
    pluses = list(filter(lambda x: x > 0, arr))
    my_id[id][2].append(sum(pluses))
    answers = list(filter(lambda x: x != 0, arr))
    my_id[id][3].append(len(answers))


new = [[x[0], *x[1][1], *x[1][2], *x[1][3]] for x in my_id.items()]
new.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
# [37961, 1, 3, 3]
new = [x for x in new if x[1] > 0]
# for i in new:
#     print(i)
# print(len(new) / 3)
# [52766, 11, 12, 5]
print(len(new) - 2383)
k = 0
arr = []
for i in range(2383, 2383 + 476 + 2):
    arr.append(new[i])
    print(new[i])
print(len(arr))
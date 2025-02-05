from itertools import chain


k = 47
s = 1263519
m = 51
data = [list(map(int, x.split())) for x in open('26.txt')]
my_types = {x: [] for x in range(1, k + 1)}
for t, v in data:
    my_types[t].append(v)
    my_types[t].sort()
total = []
for t in my_types:
    arr = my_types[t]
    for i in range(m):
        total.append(arr.pop(0))
details = list(chain.from_iterable([x for x in my_types.values()]))
details.sort()
while sum(total) + details[0] <= s:
    total.append(details.pop(0))
print(len(total))
# my_types = {x: [] for x in range(1, k + 1)}
# for t, v in data:
#     my_types[t].append(v)
#     my_types[t].sort()
# arr = list(my_types.values())
# while len(details):
#     if details[0] in arr:
#         arr.remove(details.pop(0))
#
# print(details)
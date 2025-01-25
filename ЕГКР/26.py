n = 40419
data = [list(map(int, x.split())) for x in open('26')]
id = set([x[0] for x in data])
my_nums = {}
for i in id:
    my_nums[i] = [set(), 0]
for i, task in data:
    my_nums[i][0].add(task)
for i in my_nums:
    my_nums[i][0] = sorted(list(my_nums[i][0]))
for i in my_nums:
    k = 1
    mx = 1
    arr = my_nums[i][0]
    for x in range(len(arr) - 1):
        if arr[x] == arr[x + 1] - 1:
            k += 1
        else:
            mx = max(k, mx)
            k = 1
    mx = max(k, mx)
    my_nums[i][1] = mx
new = [[x[0], x[1][1]] for x in my_nums.items()]
new.sort(key=lambda x: (-x[1], x[0]))
for i in new:
    print(*i)
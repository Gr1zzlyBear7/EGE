ans = []
for n in range(1000, 10000):
    num = list(map(int, str(n)))
    evens = sum([(x) for x in num if x % 2 == 0]) ** 2
    diff = (max(num) - min(num)) ** 3
    arr = ''.join([str(x) for x in sorted([diff, evens])])
    if arr == '4343':
        ans.append(n)
print(min(ans))
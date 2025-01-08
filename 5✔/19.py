ans = []
for n in range(10, 1000):
    nums = []
    s = str(n)
    for x in range(len(s) - 1):
        nums.append(int(s[x] + s[x + 1]))
    maxi = max(nums)
    mini = min(nums)
    r = maxi - mini
    if r == 44:
        ans.append(n)

print(min(ans))
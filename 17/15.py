s = list(map(int, open('15.txt').readlines()))
ans = []
maxi = max([x for x in s if abs(x) % 19 == 0])
for i in range(len(s) - 1):
    if len([1 for x in [s[i], s[i + 1]] if x > maxi]) >= 1:
        ans.append(sum([s[i], s[i + 1]]))
print(len(ans), min(ans))
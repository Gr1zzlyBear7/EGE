s = list(map(int, open('13.txt').readlines()))
ans = []
for i in range(len(s) - 1):
    if 50 <= abs(s[i]) + abs(s[i + 1]) <= 200:
        ans.append(min(s[i], s[i + 1]))
print(len(ans), min(ans))
s = list(map(int, open('14.txt').readlines()))
ans = []
sr = sum(s) / len(s)
for i in range(len(s) - 2):
    arr = [s[i], s[i + 1], s[i + 2]]
    if len([1 for x in arr if x > sr]) >= 2:
        ans.append(sum(arr))
print(len(ans), max(ans))
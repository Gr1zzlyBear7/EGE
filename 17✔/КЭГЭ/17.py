s = list(map(int, open('17.txt').readlines()))
ans = []
arr = [x for x in s if abs(x) % 10 == 4]
const = max(arr) + min(arr)
for i in range(len(s) - 1):
    if s[i] + s[i + 1] < const:
        ans.append(s[i] + s[i + 1])
print(len(ans), max(ans))
k = 3
m = 5
arr = set()
for x in open('26.txt').readlines():
    a, b = map(int, x.split())
    if b >= k:
        arr.add(a)
arr = sorted(arr)
ans = [arr[0]]
for i in range(1, len(arr) - 1):
    if arr[i + 1] - ans[-1] > m and arr[i] - ans[-1] <= m:
        ans.append(arr[i])
print(ans)
print(len(ans) - 1)

n = 9937
arr = [0] * 2_000_001
f = open('7')
for i in range(n):
    st, end = map(int, f.readline().split())
    arr[st] += 1
    arr[end] -= 1

k = 0
count, total = 0, 0
st, end = -1, 0
for i in range(2_000_001):
    k0 = k
    k += arr[i]
    if k > 0 and st == -1:
        st = i
    if k == 0 and k0 > 0:
        count += 1
        end = i
        total += end - st
        st, end = -1, 0
print(count, total)
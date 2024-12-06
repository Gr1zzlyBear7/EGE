s = list(map(int, open('18.txt').readlines()))
ans = []
for i in range(len(s) - 1):
    arr = [abs(s[i]), abs(s[i + 1])]
    if arr[0] % 9 == 0 and arr[1] % 9 != 0 and arr[1] % 8 == 3 or arr[0] % 9 != 0 and arr[1] % 9 == 0 and arr[
        0] % 8 == 3:
        ans.append(max(s[i], s[i + 1]))
print(len(ans), max(ans))

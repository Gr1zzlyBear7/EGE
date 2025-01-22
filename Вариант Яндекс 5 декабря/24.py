s = open('24 (18).txt').readline()
k = 1
maxi = 0
arr = []
for i in s:
    if i not in arr:
        k += 1
        arr.append(i)
    else:
        maxi = max(k, maxi)
        k = 1
        arr = []
maxi = max(k, maxi)
print(maxi)
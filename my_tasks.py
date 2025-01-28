arr = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, '19-21', 23, 24, 25, 26, 27]
arr = list(map(str, arr))
for i in range(len(arr)):
    arr[i] = arr[i] + '.py'
arr.append('27a.txt')
arr.append('27b.txt')
arr.append('26.txt')
arr.append('17.txt')
arr.append('9.txt')
print(arr)
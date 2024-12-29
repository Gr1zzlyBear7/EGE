s = list(map(int, open('16.txt').readlines()))
arr1 = [x for x in s if abs(x) % 11 == 0]
arr2 = [x for x in s if abs(x) % 17 == 0]
ans = max(arr1, arr2, key=len)
print(len(ans), min(ans))
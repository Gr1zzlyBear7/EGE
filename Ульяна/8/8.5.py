from itertools import product

arr = list(product('УОА', repeat=5))
print(''.join(arr[99]))
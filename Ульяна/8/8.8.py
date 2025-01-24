from itertools import product
al = 'АКЛМНЯ'
k = 0
arr = list(product(al, repeat=5))
print(arr.index(tuple('МНЯЯЯ')) - arr.index(tuple('МНААА')) - 1)
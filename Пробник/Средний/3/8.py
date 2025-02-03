from itertools import product, permutations
al = 'abcdef'
my = [''.join(x) for x in list(permutations('cdef'))]
k = 0
for i in permutations(al):
    if len(set(i)) == len(i):
        s = ''.join(i)
        for x in my:
            if x in s:
                break
        else:
            continue
        k += 1
print(k)
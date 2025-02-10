from itertools import product
al = '0123456789'
k = 0
for i in product(al, repeat=3):
    if i[0] != '0':
        s = ''.join(i)
        for i in range(len(s) - 1):
            if s[i] <= s[i + 1]:
                pass
            else:
                break
        else:
            k += 1
            print(s)
print(k)
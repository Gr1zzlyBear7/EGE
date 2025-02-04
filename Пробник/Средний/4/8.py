al = 'екоф'
from itertools import *
ans = []
k = 1
for i in product(al, repeat=5):
    s = ''.join(i)
    if s.count('о') == 1:
        s = s.replace('к', 'ф')
        if 'фо' not in s and 'оф' not in s:
            ans.append(k)
    k += 1
print(ans[0] + ans[-1])
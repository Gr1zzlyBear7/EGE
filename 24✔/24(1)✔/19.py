import collections
string = open('19.txt').readlines()
maxi = 0
s = 0
for i in range(len(string)):
    if string[i].count('Q') >= maxi:
        maxi = string[i].count('Q')
        s = i
md = collections.Counter(string[s])
md = md.most_common()
print(''.join(string).count(md[-2][0]))
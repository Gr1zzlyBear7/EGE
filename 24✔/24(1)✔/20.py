import collections

string = open('20.txt').readlines()
count = 0
let = ''
ans = []
for i in range(len(string)):
    k = 1
    for b in range(len(string[i]) - 1):
        if string[i][b] == string[i][b + 1]:
            k += 1
            if count < k:
                count = k
                let = string[i][b]
        else:
            k = 0
    ans.append((count, let, i))
maxi = (max(ans, key=lambda x: x[0]))
md = collections.Counter(string[maxi[2]])
print(''.join(string).count(md.most_common()[0][0]))
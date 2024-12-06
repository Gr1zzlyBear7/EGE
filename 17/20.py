s = list(map(int, open('20.txt').readlines()))
ans = []
arr = sum([sum(map(int, str(x))) for x in s if x % 35 == 0])
for i in range(len(s) - 1):
    if (s[i] > arr > s[i + 1] and hex(s[i + 1])[-2::] == 'ef' or
            s[i] < arr < s[i + 1] and hex(s[i])[-2::] == 'ef'):
        ans.append(s[i] + s[i + 1])
print(len(ans), min(ans))

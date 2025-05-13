data = list(map(int, open('26.txt')))
data.sort(reverse=True)
sub = []
ans = [data[0]]
for i in range(len(data) - 1):
    if ans[-1] - data[i] >= 9:
        ans.append(data[i])
print(len(ans), min(ans))
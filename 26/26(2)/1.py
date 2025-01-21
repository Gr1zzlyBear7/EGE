s = 100000
data = list(map(int, open('1.txt')))
data.sort()
ans = []
k = 0
while True:
    if sum(ans) + data[-1] <= s:
        ans.append(data.pop())
    else:
        new = data[::-1]
        for elem in new:
            if sum(ans) + elem <= s:
                ans.append(elem)
                data.remove(elem)
        else:
            break
    if sum(ans) + data[0] <= s:
        ans.append(data.pop(0))
    else:
        break
print(len(ans), ans[-1])
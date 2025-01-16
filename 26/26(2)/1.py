size = 100000
k = 0
data = sorted(list(map(int, open('1.txt'))))
flag = True
ans = []
for elem in data:
    if flag:
        el = max(data)
        if size - el >= 0:
            size -= el
            k += 1
            data.remove(el)
            flag = False
            ans.append(el)
        else:
            for x in data[::-1]:
                if x <= size:
                    size -= x
                    k += 1
                    data.remove(x)
                    flag = False
                    ans.append(x)
                    break
    else:
        el = min(data)
        if size - el >= 0:
            size -= el
            k += 1
            data.remove(el)
            ans.append(el)
            flag = True
        else:
            for x in data:
                if x <= size:
                    size -= x
                    k += 1
                    data.remove(x)
                    flag = False
                    ans.append(x)
                    break

print(k, ans[-1])
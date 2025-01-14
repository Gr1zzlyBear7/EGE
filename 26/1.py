maxi = 1000000
data = sorted(list(map(int, open('1.txt'))), reverse=True)
k = 0
for mem in data:
    if maxi >= mem:
        maxi -= mem
        k += 1
        mini = mem
print(mini)
print(k, maxi)
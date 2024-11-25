string = open('11.txt').readlines()
k = 0
for i in string:
    for j in range(len(i) - 3):
        if i[j] == 'K' and i[j + 2] == 'G' and i[j + 3] == 'E':
            k += 1
            break
print(k)

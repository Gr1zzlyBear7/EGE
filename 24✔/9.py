string = open('9.txt').readlines()
k = 0
for i in string:
    if i.count('S') == i.count('X'):
        k += 1
print(k)

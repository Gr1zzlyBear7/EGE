string = open('10.txt').readlines()
k = 0
for i in string:
    if i.count('B') >= i.count('A') * 1.05:
        k += 1
print(k)
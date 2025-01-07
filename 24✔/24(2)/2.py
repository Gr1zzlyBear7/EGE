s = open('2.txt').readline()

s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ')

s = s.split()

a = 0
for x in s:
    if len(x) > a:
        a = len(x)

print(a)
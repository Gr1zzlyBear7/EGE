s = open('10.txt').readline()

s = s.replace('O', 'N').replace('P', 'N')
s = s.replace('NN', 'N N')
for x in s.split():
    if len(x) == 58:
        print(x)
while 'NN' in s:
    s = s.replace('NN', 'N N')
print(max(len(x) for x in s.split()))
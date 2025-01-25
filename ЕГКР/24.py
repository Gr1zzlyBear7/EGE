s = open('24_19254.txt').readline()
k = 1
st = -1
while 'FSRQ' in s:
    s = s.replace('FSRQ', '*')
for i in range(len(s) - 1):
    if s[i] == '*':
        k += 1
        end = i
        if st == -1:
            st = i
    elif k == 80:
        print(len(s[st-4: i + 27]))
        print(1)
        break

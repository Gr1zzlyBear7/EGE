s = open('24 (12).txt').read().replace('*-', ' ').replace('--', ' ').replace('**', ' ').replace('-*', ' ')
s = s.replace('6', '7').replace('7', '8').replace('8', '9')
s = s.split()
ans = []
for x in s:
    if x[0] in '-*':
        new = ''
        if x[-1] in '-*':
            x = x[1:-1]
        else:
            x = x[1:]
        x = x.replace('*', '-').split('-')
        new = []
        for w in x:
            try:
                if w[0] == '0' and len(w) != 1:
                    if w.count('0') == len(w):
                        w = '0'
                        new.append(w)
                    else:
                        w = w[w.find('9'):]
                        new.append(w)
                elif w[0] == '0' and len(w) == 1:
                    new.append(w)
                else:
                    new.append(w)
            except:
                pass
        const = len(new)
        ans.append(len(''.join(new)) + const - 1)
print(max(ans))
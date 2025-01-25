s = open('24var01.txt').readline()
mx = 0
s = s.replace('+', '-')
while '--' in s:
    s = s.replace('--', '- -')
for x in '123':
    s = s.replace(x, '4')
for x in s.split():
    arr = x.split('-')
    arr = [x for x in arr if x]
    ans = []
    for elem in arr:
        new = elem
        if new[0] == '-':
            new = new[1:]
        if new[-1] == '-':
            new = new[:-1]
        if len(new) == new.count('0'):
            new = '0'
        elif new[0] == '0':
            new = new[new.find('4'):]
        ans.append(len(new))
    mx = max(sum(ans) + len(ans), mx)
print(mx)
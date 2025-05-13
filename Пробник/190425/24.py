s1 = '7' * 15
s2 = '1' * 12
while '77777' in s1 or '1111' in s1:
    s1 = s1.replace('77777', '11', 1)
    s1 = s1.replace('1111', '7', 1)

while '77777' in s2 or '1111' in s2:
    s2 = s2.replace('77777', '11', 1)
    s2 = s2.replace('1111', '7', 1)

z = (sum(map(int, s1)))
z1 = (sum(map(int, s2)))
print(z1 - zd)
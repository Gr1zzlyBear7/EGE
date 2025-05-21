s = 108 * '7'
while '33333' in s or '777' in s:
    s = s.replace('33333', '7', 1)
    s = s.replace('777', '3', 1)
print(s)
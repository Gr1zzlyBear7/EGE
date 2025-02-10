for n in range(4, 1000):
    s = '7' + n * '3'
    while '73' in s or '3333' in s or '1133' in s:
        s = s.replace('73', '11', 1)
        s = s.replace('3333', '7', 1)
        s = s.replace('1133', '37', 1)
    if sum(map(int, s)) == 128:
        print(n)
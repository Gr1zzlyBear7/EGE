for i in range(50, 70):
    s = i * '5'
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    print(s, i)

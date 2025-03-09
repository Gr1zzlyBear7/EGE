
for i in range((int(input()))):
    s, p = map(int, input().split())
    semi_p = p / 2
    d = semi_p ** 2 - 4 * s
    if d >= 0:
        a = (semi_p + d ** 0.5) / 2
        b = (semi_p - d ** 0.5) / 2
        str_a = "{:f}".format(a).rstrip('0')
        str_b = ("{:f}".format(b)).rstrip('0')
        if len(str_a[str_a.find('.') + 1:]) == 0 and len(str_b[str_b.find('.') + 1:]) == 0:
            print(int(a), int(b))
        else:
            print(0, 0)
    else:
        print(0, 0)

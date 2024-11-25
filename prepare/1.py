a, b, c = list(map(int, input().split()))
d, e, f = list(map(int, input().split()))


def one(a, b, c):
    return a + b > c and a + c > b and b + c > a


def two(a, b, c, d, e, f):
    t1 = sorted([a, b, c])
    t2 = sorted([d, e, f])
    return t1 == t2


f1 = one(a, b, c)
f2 = one(d, e, f)

if not f1 or not f2:
    print(0)
else:
    print(1)
    if two(a, b, c, d, e, f):
        print(1)
    else:
        print(0)

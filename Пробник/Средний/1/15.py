p = list(range(5, 41))
q = list(range(41, 55))
r = list(range(6, 54))
a = []
for x in range(1, 1000):
    f = ((x not in p) <= (x in q)) and (x in r) and (x not in a)
    if not f:
        a.append(x)
print(a)
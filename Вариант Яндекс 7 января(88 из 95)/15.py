b = [z for z in range(101, 144)]
c = [z for z in range(144, 200)]
a = set()
for x in range(1, 1000):
    if (x in a) <= ((x in b) or (x in c)):
        a.add(x)

print(a)
def divs(num):
    k = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            k += 1
            if num // i != i:
                k += 1
                if k > 2:
                    return False
    return True

z = 0
t, d = list(map(int, input().split()))
if d >= t:
    for i in range(1, t + d + 1):
        if divs(i):
            z += 1
else:
    for i in range(t - d, t + d + 1):
        if divs(i):
            z += 1
print(z)
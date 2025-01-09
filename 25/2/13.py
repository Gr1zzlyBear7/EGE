def is_prime(n):
    k = 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


k = 0
for i in range(6080068, 6080177):
    if is_prime(i):
        print(i)
print(k)
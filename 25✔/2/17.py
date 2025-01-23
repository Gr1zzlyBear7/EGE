def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(int(106732567 ** 0.25) + 1, int(152673836 ** 0.25) + 1):
    if is_prime(i):
        print(i ** 4, i ** 3)

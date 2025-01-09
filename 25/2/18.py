def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(55_000_000, 60_000_000 + 1):
    num = i
    while num % 2 == 0:
        num //= 2
    if int(num ** 0.25) ** 4 == num and is_prime(int(num ** 0.25)):
        print(i, num)


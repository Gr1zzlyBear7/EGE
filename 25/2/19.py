def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(113_000_000, 114_000_001):
    if i % 2 == 0 and i % 4 != 0:
        num = i // 2
        if int(num ** 0.5) ** 2 == num and is_prime(int(num ** 0.5)):
            print(i, 2 * int(num ** 0.5))

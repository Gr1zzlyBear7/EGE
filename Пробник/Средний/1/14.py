def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


al = '0123456789abcdefgh'
z = 0
for x in al:
    k = int(f'56{x}3', 18) + int(f'4{x}9', 18) - int(f'57{x}1', 18)
    if is_prime(k):
        print(x)
        z += 1
print(z)
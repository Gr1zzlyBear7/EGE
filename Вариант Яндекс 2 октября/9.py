const = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50

def fn(n):
  new = ''
  while n > 0:
    new += str(n % 49)
    n //= 49
  return (new[::-1])


print(sum(map(int, fn(abs(const)))))
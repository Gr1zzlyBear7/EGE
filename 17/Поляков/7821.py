data = list(map(int, open('7821').readlines()))

ans = []


def six(num):
    new = ''
    while num > 0:
        new += str(num % 6)
        num //= 6
    return int(new[::-1])


mini_5 = min([x for x in data if 1000 <= six(x) < 10000]) % 5


def nine(num):
    new = ''
    while num > 0:
        new += str(num % 9)
        num //= 9
    return int(new[::-1])


mini_13 = min([x for x in data if 100 <= nine(x) <= 999]) % 13

for i in range(len(data) - 2):
    troyka = data[i:i + 3]
    arr_11 = [x for x in troyka if x % 11 == mini_5]
    arr_7 = [x for x in troyka if x % 7 == mini_13]
    if len(arr_11) == 1 and len(arr_7) == 1:
        ans.append(sum(troyka))

print(len(ans), min(ans))

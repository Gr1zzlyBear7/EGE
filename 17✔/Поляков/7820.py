data = list(map(int, open('7820').readlines()))

ans = []

mini_11 = min([x for x in data if len(str(x)) == 4]) % 11
mini_3 = min([x for x in data if len(str(x)) == 2]) % 3

for i in range(len(data) - 2):
    troyka = data[i:i + 3]
    arr_11 = [x for x in troyka if x % 7 == mini_11]
    arr_7 = [x for x in troyka if x % 5 == mini_3]
    if len(arr_11) == 1 and len(arr_7) == 1:
        ans.append(sum(troyka))

print(len(ans), min(ans))

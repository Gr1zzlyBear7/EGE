data = list(map(int, open('7818').readlines()))

ans = []

mini_5 = min(data) % 5
maxi_7 = max(data) % 7

for i in range(len(data) - 2):
    troyka = data[i:i + 3]
    arr_5 = [x for x in troyka if x % 5 == mini_5]
    arr_7 = [x for x in troyka if x % 7 == maxi_7]
    if len(arr_7) == len(arr_5) == 1:
        ans.append(sum(troyka))
print(len(ans), min(ans))

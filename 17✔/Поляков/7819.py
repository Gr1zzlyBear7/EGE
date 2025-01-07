data = list(map(int, open('7819').readlines()))

ans = []

maxi_11 = max(data) % 11
mini_3 = min(data) % 3

for i in range(len(data) - 2):
    troyka = data[i:i + 3]
    arr_3 = [x for x in troyka if x % 3 == maxi_11]
    arr_11 = [x for x in troyka if x % 11 == mini_3]
    if len(arr_3) == 1 and len(arr_11) == 1:
        ans.append(sum(troyka))

print(len(ans), min(ans))


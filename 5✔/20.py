ans = []
for n in range(1, 1000):
    num = str(n)
    evans = [int(x) for x in num if x in '02468']
    arr = [int(num[x]) for x in range(1, len(num), 2)]
    r = abs(sum(evans) - sum(arr))
    if r == 9:
        ans.append(n)

print(min(ans))
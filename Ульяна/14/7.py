arr = []
al = '0123456789abcdef'
for x in al:
    for y in al:
        k = int(f'27a{x}23', 16) + int(f'8{y}e5d2', 16)
        if k % 5 == 0:
            arr.append(x + y)
print(max(arr))
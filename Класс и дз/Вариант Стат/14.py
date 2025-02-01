# for p in range(10, 33):
s = '0123456789'
ans = []
for i in range(ord('a'), ord('a') + 20):
    ans.append(chr(i))
al = s + ''.join(ans)
for p in range(10, 33):
    for x in al[:p]:
        for y in al[:p]:
            for z in al[:p]:
                for w in al[:p]:
                    if int(f'{y}18{x}', p) + int(f'{w}{y}98', p) == int(f'{x}{x}{z}4{y}', p):
                        print(int(f'{x}{y}{z}{w}', p))

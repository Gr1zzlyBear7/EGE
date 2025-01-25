al = '0123456789abcdef'
for p in range(16, 17):
    for x in al:
        for y in al:
            if int(f'397{x}', p) + int(f'{x}9{x}4', p) == int(f'{y}19{y}', p):
                print(int(f'{x}{x}{y}{y}', p))

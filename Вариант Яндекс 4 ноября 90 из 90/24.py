s = open('24 (15).txt').read()
maxi = 0
for i in range(len(s)):
    let = dig = 0
    for j in range(i, len(s)):
        if s[j] in 'KLMN':
            let += 1
        else:
            dig += 1
        if let == 2 * dig:
            maxi = max(maxi, let + dig)

print(maxi)
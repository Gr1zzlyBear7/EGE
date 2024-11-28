with open('6.txt') as f:
    data = list(map(int, f.readlines()))
    ans = []
    for i in range(len(data) - 1):
        n1 = data[i]
        n2 = data[i + 1]
        if abs(n2 + n1) % 3 == 0 and abs(n2 + n1) % 6 != 0:
            if abs(n2 * n1) % 10 == 8:
                ans.append(n1 + n2)
    print(len(ans), max(ans))
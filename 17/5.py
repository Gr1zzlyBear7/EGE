with open('5.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [x for x in data if hex(x)[-1] == 'b' and x % 7 == 0 and x % 6 != 0 and x % 13 != 0 and x % 19 != 0]
    print(sum(ans), len(ans))
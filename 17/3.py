with open('3.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [x for x in data if (x % 10 == 5 or x % 10 == 7) and x % 9 != 0 and x % 11 != 0]
    print(len(ans), max(ans) + min(ans))
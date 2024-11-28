with open('4.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [x for x in data if x % 13 == 7 and x % 7 != 0 and x % 11 != 0]
    print(max(ans) - min(ans), len(ans))
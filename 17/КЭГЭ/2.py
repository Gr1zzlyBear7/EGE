with open('2.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [num for num in data if (num % 10 == 2 or num % 10 == 7) and num % 3 == 0 and num % 11 == 0]
    print(len(ans), min(ans))
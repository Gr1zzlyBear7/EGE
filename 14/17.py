for x in range(3, 20):
    num = 68
    arr = []
    while num > 0:
        arr.append(num % x)
        num //= x
    if arr[0] == 2 and len(arr) == 4:
        print(x)
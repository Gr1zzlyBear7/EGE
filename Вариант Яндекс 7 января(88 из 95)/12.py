def f(n):
    s = "8" + n * "4"
    while "4444" in s or "844" in s or "84" in s:
        if "4444" in s:
            s = s.replace("4444", "884", 1)
        if "844" in s:
            s = s.replace("844", "488", 1)
        if "84" in s:
            s = s.replace("84", "3343", 1)
    if len(s) >= 20:
        return True
    return False


for N in range(4, 10000 - 1):
    if all(f(n) for n in range(N, 1000)):
        print(N)
        break

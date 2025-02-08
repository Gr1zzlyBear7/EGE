data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
arr_l = []
arr_s = []
for line in data:
    if len(set(line)) == len(line):
        a, b, c = line[0] / 100, line[1] / 100, line[2] / 100
        s = 2 * (a * b + a * c + c * b)
        if s < 10:
            arr_s.append(s)
        else:
            arr_l.append(s)
print(len(arr_l) / 103, len(arr_s) / 191)
print(7 + 12)
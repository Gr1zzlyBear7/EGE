data = [list(map(int, line.split())) for line in open('19')]
k = 0
for line in data:
    arr = [line.count(x) for x in set(line)]
    if 2 in arr and len(set(line)) == 5:
        print(1)
        arr_evans = [x for x in line if x % 2 == 0]
        arr_odds = [x for x in line if x % 2 == 1]
        sr_ev = 0 if len(arr_evans) == 0 else sum(arr_evans) / len(arr_evans)
        sr_od = 0 if len(arr_odds) == 0 else sum(arr_odds) / len(arr_odds)
        if abs(sr_ev - sr_od) <= 50:
            k += 1
    else:
        arr_evans = [x for x in line if x % 2 == 0]
        arr_odds = [x for x in line if x % 2]
        sr_ev = 0 if len(arr_evans) == 0 else sum(arr_evans) / len(arr_evans)
        sr_od = 0 if len(arr_odds) == 0 else sum(arr_odds) / len(arr_odds)
        if abs(sr_ev - sr_od) > 50:
            k += 1

print(k)
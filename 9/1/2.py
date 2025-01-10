k = 0
data = [line.split() for line in open('2', encoding='UTF-8') if
        line.split()[2] == '3' or line.split()[2] == '1' or line.split()[2] == '5']

for line in data:
    if int(line[3]) <= 36 and int(line[4]) <= 43:
        k += 1

print(k)
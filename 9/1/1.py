k = 0
data = [line.split() for line in open('1', encoding='UTF-8') if line.split()[2] == '1']

for line in data:
    if int(line[3]) >= 85 or int(line[4]) >= 85:
        k += 1
print(k)
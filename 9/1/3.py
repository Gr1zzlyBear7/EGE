data = [line.split() for line in open('3', encoding='UTF-8')]

k = 0
for line in data:
    if int(line[3]) >= 37 and int(line[4]) < 44:
        k += 1

print(k / len(data) * 100)
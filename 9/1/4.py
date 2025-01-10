data = [line.split() for line in open('4', encoding='UTF-8')]

k = 0
print(data)
for line in data:
    if int(line[3]) > int(line[4]) >= 44:
        k += 1

print(k / len(data) * 100)
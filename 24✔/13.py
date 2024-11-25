string = open('13.txt').readline()
k = 0
for i in range(len(string) - 6):
    if string[i] == 'A' and string[i + 6] == 'F':
        k += 1
for i in range(len(string) - 7):
    if string[i] == 'A' and string[i + 7] == 'F':
        k += 1
for i in range(len(string) - 8):
    if string[i] == 'A' and string[i + 8] == 'F':
        k += 1
for i in range(len(string) - 9):
    if string[i] == 'A' and string[i + 9] == 'F':
        k += 1
print(k)
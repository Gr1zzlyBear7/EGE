string = open('8.txt').readline()
k = 0
for i in range(len(string) - 4):
    if string[i] == 'A' and string[i + 2] == 'A' and string[i + 4] == 'A':
        k += 1
print(k)
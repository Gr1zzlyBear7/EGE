string = open('14.txt').readline()
k = c = 0
for i in range(len(string) - 4):
    const = string[i:i + 5]
    if const == const[::-1]:
        k += 1
    if string[i] == string[i + 4] and string[i + 1] == string[i + 3]:
        c += 1
print(k)
print(c)

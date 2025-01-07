import fnmatch

string = open('7.txt').readline()
k = 0
for i in range(len(string) - 3):
    if string[i] == 'G' and string[i + 2] == 'M' and string[i + 3] == 'E':
        k += 1
print(k)
# print(string.count(fnmatch.fnmatch('G*ME')))
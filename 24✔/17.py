string = open('17.txt').readline()
ans = ''
for i in range(len(string) - 2):
    if string[i] == string[i + 2]:
        ans += string[i + 1]
print(ans.count('W'))
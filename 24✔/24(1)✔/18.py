string = open('18.txt').readline()
ans = ''
for i in range(len(string) - 4):
    if string[i] == 'C' and string[i + 1] == 'B' and string[i + 3] == 'B' and string[i + 4] == 'C':
        ans += string[i + 2]
print(ans.count(max(ans, key=ans.count)), max(ans, key=ans.count))
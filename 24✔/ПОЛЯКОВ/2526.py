s = open('files/2526.txt').readline()
nums = []
sub = ''
for i in range(len(s)):
    if s[i].isdigit():
        sub += s[i]
    else:
        if sub:
            nums.append(int(sub))
        sub = ''
print(min([x for x in nums if x % 2 == 0]))
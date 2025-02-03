s = open('files/2524.txt').readline()
sub = ''
nums = []
for i in range(len(s)):
    if s[i].isdigit():
        sub += s[i]
    else:
        if sub:
            nums.append(sub)
        sub = ''
print(min([int(x) for x in nums if int(x) % 2 == 1]))
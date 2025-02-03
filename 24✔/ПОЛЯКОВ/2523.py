s = open('2523.txt').readline()
nums = []
sub = ''
for i in range(len(s)):
    if s[i].isdigit():
        sub += s[i]
    else:
        if sub:
            nums.append(sub)
        sub = ''
print(max([int(x) for x in nums if int(x) % 2 == 1]))
s = open('files/2527.txt').readline()
nums = []
sub = ''
for i in range(len(s)):
    if s[i].isdigit():
        sub += s[i]
    else:
        if sub:
            if all([True if int(x) % 2 == 1 else False for x in sub]):
                nums.append(int(sub))
        sub = ''
print(max(nums))
s = open('4.txt').readline()

s = s.replace('XY', 'X Y').replace('XZ', 'X Z')
print(s)
print(max([len(x) for x in s.split()]))
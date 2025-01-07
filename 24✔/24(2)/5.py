s = open('5.txt').readline()

s = s.replace('PP', 'P P')
print(max([len(x) for x in s.split()]))
import collections

string = open('24_2509 (4).txt').readline().strip()
my = {x: string.count(x) for x in sorted(set(string))}
print(max(my.values()) - min(my.values()))
md = collections.Counter(string)
md = md.most_common()

print(md[0][1] - md[-1][1])

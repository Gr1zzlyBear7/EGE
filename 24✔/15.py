import collections

string = list(open('15.txt').readline())
md = collections.Counter(string)
md = md.most_common()
print(md[0])
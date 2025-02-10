d_size = 5000
e_size = 1500
data = list(map(int, open('26.txt')))
d_files = list(filter(lambda x: x > 500, data))
d_files.sort()
e_files = list(filter(lambda x: x <= 500, data))
e_files.sort()
total_d = []
while sum(total_d) + d_files[0] <= d_size:
    total_d.append(d_files.pop(0))
total_e = []
while sum(total_e) + e_files[0] <= e_size:
    total_e.append(e_files.pop(0))
print(total_e, total_d)
print(d_files)
for file in e_files:
    if sum(total_e) - total_e[-1] + e_files[-1] <= e_size:
        total_e[-1] = e_files.pop()
for file in d_files:
    if sum(total_d) - total_d[-1] + d_files[-1] <= d_size:
        total_d[-1] = d_files.pop()
print(len(total_e) + len(total_d), total_e[-1] + total_d[-1])
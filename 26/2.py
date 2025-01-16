maxi_d = 0
maxi_e = 0
k = 0
size_d = 5000
size_e = 1500
data = sorted(list(map(int, open('2.txt'))))
d_size = list(filter(lambda x: x > 500, data))
e_size = list(filter(lambda x: x <= 500, data))
for mem in d_size:
    if size_d >= mem:
        size_d -= mem
        k += 1
        if mem > maxi_d:
            maxi_d = mem
for mem in e_size:
    if size_e >= mem:
        size_e -= mem
        k += 1
        if mem > maxi_e:
            maxi_e = mem

print(k, maxi_d + maxi_e)

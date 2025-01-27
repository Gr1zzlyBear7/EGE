data = list(map(int, open('26')))
memory = sum(data)
data.sort()
need = (len(data) * 0.05)
print(need)
for i in range(500):
    memory -= data.pop(0)
for i in range(500):
    memory -= data.pop()

print(memory, max(data))

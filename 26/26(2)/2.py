data = list(map(int, open('2')))
large = []
tiny = []
data.sort()
k = 0

while True:
    if sum(tiny) >= sum(large):
        large.append(data.pop())
        k += 1
    else:
        tiny.append(data.pop(0))
        k += 1
    if k == 6666:
        break

print(len(large), len(tiny))
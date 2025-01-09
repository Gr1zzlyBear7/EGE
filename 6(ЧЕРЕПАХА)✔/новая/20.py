from turtle import *

tracer(0)
arr = []
k = 20
screensize(3000, 3000)
lt(90)

for i in range(2):
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 6 * k, arr[-1] + 2 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 0 * k, arr[-1] - 2 * k)

for i in range(3):
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 2 * k, arr[-1] - 1 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] - 2 * k, arr[-1] - 1 * k)

for i in range(6):
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] - 2 * k, arr[-1] + 1 * k)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
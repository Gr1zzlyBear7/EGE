from turtle import *

lt(90)
screensize(3000, 3000)
k = 20
tracer(0)
arr = []
for i in range(3):
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] - 3 * k, arr[-1] - 4 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] - 12 * k, arr[-1] - 5 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] - 0 * k, arr[-1] + 1 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 15 * k, arr[-1] + 8 * k)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
from turtle import *

tracer(0)
k = 20
lt(90)
screensize(3000, 3000)

arr = []

for i in range(5):
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 6 * k, arr[-1] + 8 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] - 8 * k, arr[-1] + 4 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 2 * k, arr[-1] - 12 * k)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
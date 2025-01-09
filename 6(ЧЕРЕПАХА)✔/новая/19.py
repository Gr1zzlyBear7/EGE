from turtle import *

tracer(0)
lt(90)
k = 20
screensize(3000, 3000)

arr = []

for i in range(5):
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 5 * k, arr[-1] + 4 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 4 * k, arr[-1] - 4 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] - 7 * k, arr[-1] - 2 * k)
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] - 2 * k, arr[-1] + 2 * k)

pu()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'purple')

done()
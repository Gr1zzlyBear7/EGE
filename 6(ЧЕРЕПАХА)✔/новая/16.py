from turtle import *

k = 30
lt(90)
screensize(3000, 3000)
tracer(0)
arr = []
for i in range(10):
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 3 * k, arr[-1] + 6 * k)
    dot(5, 'red')
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] + 7 * k, arr[-1] - 2 * k)
    dot(5, 'red')
    pos = position()
    arr.append(pos[0])
    arr.append(pos[1])
    goto(arr[-2] - 10 * k, arr[-1] - 4 * k)
    dot(5, 'red')
pu()
for x in range(-10, 40):
    for y in range(-10, 40):
        goto(x * k, y * k)
        dot(5, 'red')
done()
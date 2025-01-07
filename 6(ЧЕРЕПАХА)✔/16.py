from turtle import *

screensize(3000, 3000)
k = 20
lt(90)
tracer(0)

for i in range(2):
    arr = pos()
    goto(arr[0] + 6 * k, arr[1] + 2 * k)
    arr = pos()
    goto(arr[0] + 0 * k, arr[1] - 2 * k)
for i in range(3):
    arr = pos()
    goto(arr[0] + 2 * k, arr[1] - 1 * k)
    arr = pos()
    goto(arr[0] - 2 * k, arr[1] - 1 * k)
for i in range(6):
    arr = pos()
    goto(arr[0] - 2 * k, arr[1] + 1 * k)

pu()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5, 'red')
done()
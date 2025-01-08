from turtle import *

screensize(10000, 3000)
k = 20
tracer(0)
lt(90)

for i in range(7):
    arr = pos()
    goto(arr[0] + 6 * k, arr[1] - 9 * k)
    arr = pos()
    goto(arr[0] - 6 * k, arr[1] + 2 * k)
    arr = pos()
    goto(arr[0] + 12 * k, arr[1] + 3 * k)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
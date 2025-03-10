from turtle import *

tracer(0)
lt(90)
k = 20
screensize(3000, 3000)

for i in range(5):
    arr = pos()
    goto(arr[0] + 5 * k, arr[1] + 4 * k)
    arr = pos()
    goto(arr[0] + 4 * k, arr[1] - 4 * k)
    arr = pos()
    goto(arr[0] - 7 * k, arr[1] - 2 * k)
    arr = pos()
    goto(arr[0] - 2 * k, arr[1] + 2 * k)

pu()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5, 'red')
done()
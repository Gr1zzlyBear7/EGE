from turtle import *

tracer(0)
k = 20
lt(90)
screensize(3000, 3000)

for i in range(3):
    arr = pos()
    goto(arr[0] - 3 * k, arr[1] - 4 * k)
    arr = pos()
    goto(arr[0] - 12 * k, arr[1] - 5 * k)
    arr = pos()
    goto(arr[0] + 15 * k, arr[1] + 8 * k)
    arr = pos()
    goto(arr[0], arr[1] + 1 * k)

print((15 ** 2 + 64) ** 0.5 + 1 + 5 + 13)

pu()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5, 'red')
done()


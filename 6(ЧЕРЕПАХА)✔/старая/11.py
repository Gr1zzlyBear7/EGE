from turtle import *

tracer(0)
screensize(3000, 3000)
lt(90)
k = 20

for i in range(10):
    arr = pos()
    goto(arr[0] + 4 * k, arr[1] + 3 * k)
    arr = pos()
    goto(arr[0] - 4 * k, arr[1] + 10 * k)
    arr = pos()
    goto(arr[0] + 18 * k, arr[1] - 12 * k)
    arr = pos()
    goto(arr[0] - 24 * k, arr[1] - 12 * k)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
print(22 + 21 * 9)
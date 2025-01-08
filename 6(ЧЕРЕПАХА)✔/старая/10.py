from turtle import *

tracer(0)
lt(90)
screensize(10000, 10000)
k = 20

for i in range(15):
    arr = pos()
    goto(arr[0] + 10 * k, arr[1] + 10 * k)
    arr = pos()
    goto(arr[0] + 3 * k, arr[1] - 6 * k)
    arr = pos()
    goto(arr[0] - 9 * k, arr[1] + 3 * k)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
print(15 * 13)
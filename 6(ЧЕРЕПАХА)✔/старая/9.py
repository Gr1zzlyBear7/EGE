from turtle import *

tracer(0)
screensize(3000, 3000)
k = 20
lt(90)

for i in range(10):
    arr = pos()
    goto((arr[0] + 3 * k), (arr[1] + 6 * k))
    arr = pos()
    goto((arr[0] + 7 * k), (arr[1] + -2 * k))
    arr = pos()
    goto((arr[0] + -10 * k), (arr[1] + -4 * k))

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()

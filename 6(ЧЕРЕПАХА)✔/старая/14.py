from turtle import *

tracer(0)
lt(90)
k = 20
screensize(3000, 3000)

for i in range(5):
    arr = pos()
    goto(arr[0] + 6 * k, arr[1] + 8 * k)
    arr = pos()
    goto(arr[0] - 8 * k, arr[1] + 4 * k)
    arr = pos()
    goto(arr[0] + 2 * k, arr[1] - 12 * k)

pu()
print((12 ** 2 + 4) ** 0.5 + (64 + 16) ** 0.5 + (36 + 64) ** 0.5)
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5, 'red')
done()
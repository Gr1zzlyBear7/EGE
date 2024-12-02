from turtle import *

tracer(0)
lt(90)
screensize(3000, 3000)
k = 20

for i in range(3):
    arr = pos()
    goto(arr[0] + 90 * k, arr[1] + 90 * k)
    arr = pos()
    goto(arr[0] - 60 * k, arr[1] + 0 * k)
    arr = pos()
    goto(arr[0] - 30 * k, arr[1] - 90 * k)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
k = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if y > x and 3 * x > y and y < 90:
            k += 1
print(k)

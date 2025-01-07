from turtle import *

screensize(3000, 3000)
k = 20
lt(90)
tracer(0)
for i in range(15):
    fd(3 * k)
    rt(40)
pu()
for x in range(1, 30):
    for y in range(1, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
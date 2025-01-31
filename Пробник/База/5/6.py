from turtle import *

tracer(0)
k = 20
screensize(3000, 3000)
lt(90)

for i in range(4):
    fd(2 * k)
    rt(90)

pu()
fd(10 * k)
lt(180)

pd()

for i in range(4):
    fd(23 * k)
    rt(90)
    fd(3 * k)
    rt(90)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
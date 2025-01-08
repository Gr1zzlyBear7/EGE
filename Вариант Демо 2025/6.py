from turtle import *

tracer(0)
screensize(3000, 3000)
k = 20
lt(90)

for i in range(9):
    fd(22 * k)
    rt(90)
    fd(6 * k)
    rt(90)

pu()

fd(k)
rt(90)
fd(5 * k)
lt(90)

pd()

for i in range(9):
    fd(53 * k)
    rt(90)
    fd(75 * k)
    rt(90)

pu()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(5, 'red')
done()
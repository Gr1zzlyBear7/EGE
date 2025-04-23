from turtle import *

k = 30
lt(90)
tracer(0)
screensize(3000, 3000)

for i in range(2):
    fd(28 * k)
    rt(90)
    fd(18 * k)
    rt(90)

pu()

fd(14 * k)
rt(90)
fd(10 * k)
lt(90)

pd()

for i in range(2):
    fd(30 * k)
    rt(90)
    fd(7 * k)
    rt(90)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
from turtle import *

k = 30
tracer(0)
lt(90)
screensize(3000, 3000)
rt(30)
fd(4 * k)
rt(330)

pd()

fd(4 * k)
rt(90)
fd(7 * k)
rt(45)
fd(4 * 2 ** 0.5 * k)
rt(135)
fd(11 * k)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
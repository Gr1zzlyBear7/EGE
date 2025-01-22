from turtle import *

lt(90)
tracer(0)
k = 60
screensize(3000, 3000)

for i in range(6):
    fd(7 * k)
    rt(120)

pu()

fd(3 * k)
rt(90)

pd()

for i in range(8):
    fd(5 * k)
    rt(90)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()

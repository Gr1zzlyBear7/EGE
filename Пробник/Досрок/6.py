from turtle import *

lt(90)
tracer(0)
screensize(3000, 3000)
k = 70
rt(30)
for i in range(30):
    rt(150)
    fd(6 * k)
    rt(30)
    fd(12 * k)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
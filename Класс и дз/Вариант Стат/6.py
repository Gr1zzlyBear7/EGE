from turtle import *

lt(90)
tracer(0)
screensize(3000, 3000)
k = 30

for i in range(3):
    fd(20 * k)
    rt(90)
    fd(4 * k)
    rt(90)

for i in range(3):
    fd(6 * k)
    rt(90)
    fd(13 * k)
    rt(90)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
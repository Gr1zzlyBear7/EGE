from turtle import *

k = 40
tracer(0)
lt(90)
screensize(3000, 3000)

rt(90)

for i in range(7):
    rt(45)
    fd(11 * k)
    rt(45)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()

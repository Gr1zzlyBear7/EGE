from turtle import *

tracer(0)
lt(90)
k = 20
screensize(3000, 3000)

for i in range(4):
    fd(10 * k)
    rt(90)

pu()

for x in range(-30, 40):
    for y in range(-30, 40):
        goto(x * k, y * k)
        dot(5, 'red')

done()
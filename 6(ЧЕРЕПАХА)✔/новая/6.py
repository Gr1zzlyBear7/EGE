from turtle import *

tracer(0)
screensize(3000, 3000)
k = 20
lt(90)

for i in range(15):
    fd(7 * k)
    rt(30)
    fd(8 * k)
    rt(150)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
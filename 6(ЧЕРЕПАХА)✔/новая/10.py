from turtle import *

tracer(0)
k = 20
lt(90)
screensize(3000, 3000)

for i in range(3):
    pd()

    for j in range(2):
        fd(7 * k)
        rt(90)
        fd(7 * k)
        rt(90)

    pu()

    fd(6 * k)
    rt(90)
    fd(6 * k)
    lt(90)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
from turtle import *

k = 10
lt(90)
screensize(3000, 3000)
tracer(0)

fd(10 * k)
pd()
for i in range(6):
    fd(50 * k)
    rt(90)
    fd(43 * k)
    rt(90)

pu()
fd(40 * k)
rt(90)
fd(40 * k)
pd()
for i in range(9):
    fd(40 * k)
    lt(90)
    fd(20 * k)
    lt(90)

pu()
for x in range(0, 100):
    for y in range(0, 100):
        goto(x * k, y * k)
        dot(5, 'red')

done()
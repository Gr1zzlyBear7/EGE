from turtle import *
k = 20
lt(90)
screensize(5000, 5000)
tracer(0)

for i in range(9):
    fd(50 * k)
    rt(90)
    fd(35 * k)
    rt(90)

pu()
fd(5 * k)
rt(90)
fd(10 * k)
rt(90)
pd()

for i in range(4):
    fd(35 * k)
    rt(90)
    fd(17 * k)
    rt(90)

pu()

for x in range(-30, 60):
    for y in range(-30, 60):
        goto(x * k, y * k)
        dot(5, 'red')

done()
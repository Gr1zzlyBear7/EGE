from turtle import *

lt(90)
k = 20
screensize(3000, 3000)
tracer(0)

for i in range(2):
    fd(23 * k)
    lt(90)
    bk(27 * k)
    lt(90)

pu()
bk(5 * k)
rt(90)
fd(11 * k)
lt(90)

pd()

for i in range(2):
    fd(26 * k)
    rt(90)
    fd(32 * k)
    rt(90)

pu()

for x in range(-30, 50):
    for y in range(-50, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
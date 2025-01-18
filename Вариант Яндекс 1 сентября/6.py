from turtle import *

k = 20
tracer(0)
lt(90)
screensize(3000, 3000)

for i in range(9):
    fd(7 * k)
    rt(90)
    fd(42 * k)
    rt(90)
pu()

bk(10 * k)
lt(90)
bk(16 * k)

pd()

for i in range(9):
    fd(42 * k)
    rt(90)
    fd(16 * k)
    rt(90)

pu()

for x in range(-30, 100):
    for y in range(-30, 100):
        goto(x * k, y * k)
        dot(5, 'red')

done()

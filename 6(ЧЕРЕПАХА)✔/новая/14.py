from turtle import *

tracer(0)
lt(90)
screensize(3000, 3000)
k = 20

rt(270)
for i in range(8):
    fd(10 * k)
    rt(45)
    fd(10 * k)
    rt(135)

for i in range(4):
    fd(4 * k)
    rt(90)

pu()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'red')

done()
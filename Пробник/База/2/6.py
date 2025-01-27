from turtle import *

tracer(0)
lt(90)
k = 30
screensize(3000, 3000)

lt(180)
for i in range(3):
    rt(45)
    fd(12 * k)
    rt(45)

lt(315)
fd(12 * k)

for i in range(2):
    rt(90)
    fd(12 * k)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
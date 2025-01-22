from turtle import *

lt(90)
tracer(0)
k = 40
screensize(3000, 3000)

for i in range(7):
    rt(90)
    fd(7 * k)
    rt(90)
    fd(6 * k)

pu()

rt(90)
fd(3 * k)
rt(90)
fd(k)

pd()

for i in range(4):
    rt(90)
    fd(6 * k)
    rt(90)
    fd(11 * k)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
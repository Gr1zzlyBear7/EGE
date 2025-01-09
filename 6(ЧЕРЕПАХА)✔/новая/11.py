from turtle import *

lt(90)
screensize(3000, 3000)
k = 20
tracer(0)

for i in range(2):
    fd(24 * k)
    rt(90)
    fd(10 * k)
    rt(90)

fd(3 * k)
lt(90)
fd(13 * k)
rt(90)

for i in range(2):
    fd(9 * k)
    rt(90)
    fd(32 * k)
    rt(90)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
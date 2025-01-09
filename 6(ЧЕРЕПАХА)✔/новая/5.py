from turtle import *

tracer(0)
lt(90)
screensize(3000, 3000)
k = 20

fd(9 * k)
rt(90)

for i in range(2):
    fd(3 * k)
    rt(90)
    fd(3 * k)
    rt(270)

for i in range(2):
    fd(3 * k)
    rt(90)

fd(9 * k)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
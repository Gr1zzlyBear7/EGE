from turtle import *

tracer(0)
screensize(3000, 3000)
lt(90)
k = 20
for i in range(14):
    for j in range(3):
        fd(3 * k)
        rt(90)
    lt(180)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()

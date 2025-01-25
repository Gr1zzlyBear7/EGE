from turtle import *

tracer(0)
lt(90)
screensize(3000, 3000)
k = 30
for i in range(8):
    fd(16 * k)
    rt(90)
    fd(22 * k)
    rt(90)
pu()
fd(5 * k)
rt(90)
fd(5 * k)
lt(90)
pd()
for i in range(8):
    fd(52 * k)
    rt(90)
    fd(77 * k)
    rt(90)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
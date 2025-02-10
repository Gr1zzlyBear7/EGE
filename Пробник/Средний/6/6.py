from turtle import *
tracer(0)
k = 30
screensize(3000, 3000)
for i in range(20):
    fd(10 * k)
    rt(180)
    fd(10 * k)
    rt(198)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
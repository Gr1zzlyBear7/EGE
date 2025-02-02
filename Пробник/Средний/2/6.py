from turtle import *
tracer(0)
lt(90)
k = 30
screensize(3000, 3000)
for i in range(14):
    for z in range(3):
        fd(3 * k)
        rt(90)
    lt(180)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
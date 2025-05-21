from turtle import *

k = 70
tracer(0)
lt(90)
screensize(3000, 3000)

for i in range(12):
    rt(60)
    fd(k)
    rt(60)
    fd(k)
    rt(270)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
from turtle import *

k = 55
tracer(0)
screensize(3000, 3000)
lt(90)

rt(60)
fd(4 * k)
rt(120)

for i in range(4):
    fd(3 * k)
    rt(240)
    fd(3 * k)
    rt(120)

fd(4 * k)
rt(90)
fd(8 * 3 ** 0.5 * k)
rt(90)
fd(8 * k)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()

from turtle import *

tracer(0)
screensize(3000, 3000)
k = 20
lt(90)

for i in range(5):
    fd(35 * k)
    rt(90)
    fd(24 * k)
    rt(90)

pu()
rt(90)
fd(7 * k)
rt(90)
fd(5 * k)
pd()
for i in range(1001):
    rt(90)
    fd(20 * k)
    rt(90)
    fd(36 * k)

pu()

for x in range(-30, 50):
    for y in range(-30, 50):
        goto(x * k, y * k)
        dot(5, 'red')

done()
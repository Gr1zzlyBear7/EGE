from turtle import *

lt(90)
screensize(3000, 3000)
k = 100
tracer(0)

for i in range(36):
    fd(k)
    rt(36)
pu()
fd(4 * k)
rt(90)
pd()
for i in range(6):
    fd(6 * k)
    rt(90)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
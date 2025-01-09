from turtle import *

tracer(0)
k = 20
lt(90)
screensize(3000, 3000)

for i in range(2):
    fd(21 * k)
    rt(90)
    fd(27 * k)
    rt(90)

pu()

fd(9 * k)
rt(90)
fd(10 * k)
lt(90)

pd()

for i in range(2):
    fd(86 * k)
    rt(90)
    fd(47 * k)
    rt(90)

pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5, 'red')

done()
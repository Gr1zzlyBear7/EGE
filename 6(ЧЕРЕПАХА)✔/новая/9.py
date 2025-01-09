from turtle import *

tracer(0)
lt(90)
screensize(3000, 3000)
k = 20

for i in range(5):
    fd(15 * k)
    lt(90)
    fd(25 * k)
    lt(90)

pu()

fd(4 * k)
lt(90)
fd(12 * k)
lt(90)

pd()

for i in range(6):
    fd(38 * k)
    rt(90)
    fd(22 * k)
    rt(90)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
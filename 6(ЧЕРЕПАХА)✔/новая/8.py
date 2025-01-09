from turtle import *

tracer(0)
lt(90)
screensize(3000, 3000)
k = 20

for i in range(3):
    fd(7 * k)
    rt(90)

fd(8 * k)

for i in range(3):
    lt(90)
    fd(5 * k)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
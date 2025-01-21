from turtle import *

k = 50
lt(90)
screensize(3000, 3000)
tracer(0)

for i in range(42):
    rt(60)
    fd(7 * k)
    rt(60)

pu()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(5, 'red')

done()
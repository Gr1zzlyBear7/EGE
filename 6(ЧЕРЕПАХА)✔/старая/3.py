from turtle import *

tracer(0)
k = 20
lt(90)
screensize(3000, 3000)
for i in range(11):
    fd(4 * k)
    rt(60)
pu()
for x in range(1, 30):
    for y in range(1, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
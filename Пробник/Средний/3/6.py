from turtle import *
lt(90)
screensize(3000, 3000)
k = 50
tracer(0)
lt(15)
for i in range(7):
    lt(30)
    fd(10 * k)
    lt(60)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
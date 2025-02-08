from turtle import *
k = 40
lt(90)
screensize(3000, 3000)
tracer(0)
for i in range(8):
    fd(12 * k)
    rt(90)
pu()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'red')
done()
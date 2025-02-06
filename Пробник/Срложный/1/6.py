from turtle import *
lt(90)
k = 50
screensize(3000, 3000)
tracer(0)

for i in range(19):
    fd(8 * k)
    rt(110)
    fd(8 * k)
    rt(70)

pu()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'red')
done()
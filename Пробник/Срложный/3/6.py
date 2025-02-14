from turtle import *
k = 60
lt(90)
screensize(3000, 3000)
tracer(0)
for i in range(3):
    fd(10 * k)
    rt(120)
pu()
fd(10 * k)
rt(90)
fd(3 * k)

pd()

for i in range(4):
    fd(10 * k)
    rt(90)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
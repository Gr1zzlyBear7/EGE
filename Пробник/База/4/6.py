from turtle import *
k = 20
screensize(3000, 3000)
lt(90)
tracer(0)
for i in range(6):
    fd(10 * k)
    rt(90)

fd(2 * k)
rt(90)

for i in range(2):
    fd(15 * k)
    rt(90)
    fd(4 * k)
    rt(90)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
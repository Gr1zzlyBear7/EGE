from turtle import *
lt(90)
tracer(0)
k = 30
screensize(3000, 3000)
for i in range(6):
    fd(25 * k)
    rt(120)
pu()
fd(20 * k)
lt(90)
bk(5 * k)

pd()

for i in range(2):
    fd(20 * k)
    lt(90)
    fd(10 * k)
    lt(90)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
done()
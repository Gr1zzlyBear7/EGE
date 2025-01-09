from turtle import *

tracer(0)
lt(90)
lt(255)
screensize(3000, 3000)
k = 30

for i in range(3):
    lt(30)
    for j in range(4):
        fd(10 * k)
        lt(90)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()
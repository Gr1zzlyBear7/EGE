from turtle import *

tracer(0)
k = 100
screensize(3000, 3000)
lt(90)

for i in range(16):
    lt(36)
    fd(4 * k)
    lt(36)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')

done()

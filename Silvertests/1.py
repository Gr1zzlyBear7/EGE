# for i in range(1, 5):
#     open(str(i) + '.py', mode='a')

from turtle import *

k = 20
tracer(0)
lt(45)

screensize(3000, 3000)
for i in range(5):
    for j in range(3):
        fd(4 * k)
        lt(90)
    fd(2 * k)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5, 'red')
pd()
done()
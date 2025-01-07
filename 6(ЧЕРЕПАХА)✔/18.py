from turtle import *

tracer(0)
k = 20
lt(90)
screensize(10000, 3000)

for i in range(2):
    arr = pos()
    goto(arr[0] + 5 * k, arr[1] + 15 * k)
    arr = pos()
    goto(arr[0] + 111 * k, arr[1] + 0 * k)
    arr = pos()
    goto(arr[0] - 60 * k, arr[1] - 15 * k)
    arr = pos()
    goto(arr[0] - 56 * k, arr[1] + 0 * k)

pu()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x * k, y * k)
#         dot(5, 'red')
done()
k = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if 3 * x > y and 0.25 * x - 14 < y and y < 15 and y > 0:
            k += 1
print(k)

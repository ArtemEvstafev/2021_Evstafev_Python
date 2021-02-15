import turtle as t

t.shape('turtle')
t.speed(10)


def go():
    t.forward(1)


def left(n):
    t.left(n)


def right(n):
    t.right(n)


t.speed(10)

for n in range(0, 360):
    go()
    left(1)
for n in range(0, 360):
    go()
    right(1)
left(45)
for n in range(0, 360):
    go()
    left(1)
for n in range(0, 360):
    go()
    right(1)
left(90)
for n in range(0, 360):
    go()
    left(1)
for n in range(0, 360):
    go()
    right(1)
input()

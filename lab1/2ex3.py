import turtle as t

t.shape('circle')
t.shapesize(0.1, 0.1, 1)
t.speed(10)
dt = 0
ay = 9.8
y = 0
x = -300
Vx = 5  # pix/sec
Vy = 60  # pix/sec
t.forward(300)
t.right(180)
t.forward(600)
t.right(180)
while True:
    dt = 0.1
    x += Vx * dt
    y += Vy * dt - ay * dt ** 2 / 2
    Vy -= ay * dt
    if y <= 0:
        Vy *= -0.95
        Vx *= 0.9
    t.goto(x, y)

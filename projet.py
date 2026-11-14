import turtle

t = turtle.Turtle()
t.speed(0)

t.up()
t.goto(20, -300)
t.down()

tg = ["navy", "cyan", "blue"]

cote = 400

for i in range(100):
    t.color(tg[i % 3])

    for _ in range(4):
        t.forward(cote)
        t.left(90)

    t.forward(cote * 0.03)
    t.left(1.8)
    cote *= 0.97

turtle.done()

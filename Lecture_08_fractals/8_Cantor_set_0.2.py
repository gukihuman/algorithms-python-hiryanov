import turtle

def go_down(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def cantor(l, n, x=0, y=0, first=True):
    if first:
        go_down(x, y)
        turtle.forward(l)
        cantor(l / 3, n, x, y - 20, False)
        return
    if n <= 0:
        return
    if n == 1:
        go_down(x, y)
        turtle.forward(l)
        turtle.penup()
        turtle.forward(l)
        turtle.pendown()
        turtle.forward(l)
        return
    go_down(x, y)
    turtle.forward(l)
    cantor(l / 3, n - 1, x, y - 20, False)
    turtle.penup()
    turtle.goto(x + l, y)
    turtle.forward(l)
    turtle.pendown()
    turtle.forward(l)
    cantor(l / 3, n - 1, x + (l * 2), y - 20, False)

cantor(800, 6, -400, 100)
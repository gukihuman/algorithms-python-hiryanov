import turtle

def line(l, n):
    if n == 0:
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
        turtle.right(120)
        turtle.forward(l)
        turtle.left(60)
        turtle.forward(l)
        return
    line(l/3, n - 1)
    turtle.left(60)
    line(l/3, n - 1)
    turtle.right(120)
    line(l/3, n - 1)
    turtle.left(60)
    line(l/3, n - 1)

def star(l, n):
    line(l, n)
    turtle.right(120)
    line(l, n)
    turtle.right(120)
    line(l, n)


turtle.penup()
turtle.goto(-250,150)
turtle.pendown()
turtle.speed('fastest')
star(150,4)
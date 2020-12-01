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

turtle.penup()
turtle.goto(-400,0)
turtle.pendown()
turtle.speed('fastest')
line(275, 5)
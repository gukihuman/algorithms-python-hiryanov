import turtle

def cantor(l, n, deep=1):
    if deep == 1:
        turtle.forward(l)
        turtle.penup()
        turtle.goto(0, -20)
        turtle.pendown()
        cantor(l/3, n - 1, deep + 1)
        return
    if n == 0:
        turtle.forward(l)
        turtle.penup()
        turtle.forward(l)
        turtle.pendown()
        turtle.forward(l)
        turtle.penup()
        turtle.left(90)
        turtle.forward(20)
        return
    turtle.forward(l)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(180)
    turtle.pendown()
    cantor(l/3, n - 1, deep)
    turtle.forward(20*(n-1))
    turtle.right(90)
    turtle.forward(l)
    turtle.pendown()
    turtle.forward(l)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(180)
    turtle.pendown()
    cantor(l/3, n - 1, deep)

cantor(300, 5)
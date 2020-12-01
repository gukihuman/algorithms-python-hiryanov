import turtle

def levy(l, n):
    if n == 0:
        turtle.left(45)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        turtle.left(45)
        return
    turtle.left(45)
    levy((l**2/2)**0.5, n-1)
    turtle.right(90)
    levy((l**2/2)**0.5, n-1)
    turtle.left(45)
turtle.penup()
turtle.goto(-225,-175)
turtle.pendown()
turtle.speed('fastest')
levy(320, 6)
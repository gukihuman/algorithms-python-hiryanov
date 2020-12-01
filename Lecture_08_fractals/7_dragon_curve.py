import turtle

def side(l):
    return (l**2/2)**0.5

def dragon(l, n, turn='right'):
    if n == 0:
        turtle.forward(l)
        return

    if turn == 'right':
        turtle.right(45)
    else: # turn == 'left'
        turtle.left(45)

    dragon(side(l), n - 1, turn='right')

    if turn == 'right':
        turtle.left(90)
    else: # turn == 'left'
        turtle.right(90)

    dragon(side(l), n - 1, turn='left')

    if turn == 'right':
        turtle.right(45)
    else: # turn == 'left'
        turtle.left(45)

turtle.speed('fastest')

dragon(400, 12)
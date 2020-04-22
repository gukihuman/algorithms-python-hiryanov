import math
import graphics as gr

def checkMouse(self):
    """Return last mouse click or None if mouse has
    not been clicked since last call"""
    if self.isClosed():
        raise GraphicsError("checkMouse in closed window")
    self.update()
    if self.mouseX != None and self.mouseY != None:
        x,y = self.toWorld(self.mouseX, self.mouseY)
        self.mouseX = None
        self.mouseY = None
        return Point(x,y)
    else:
        return None

def add(point_1, point_2):
    """Return an addition of the two arguments.
    Working with graphic type Point"""
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point

def sub (point_1, point_2):
    """Return a substraction of the second argument from the first.
    Working with graphic type Point"""
    new_point = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)
    return new_point

def update_theta():
    """Return the angle starting in the top of the pendelum using
    a right triangle with right down point in the starting coordinates
    and the left down point in the middle of the pendulum"""
    sin = (coords.x - top_pen.x) / (top_pen.y - start_point.y)
    return math.atan(sin)

def update_height():
    """Return the line between the top point of the pendulum and
    the middle point of the pendulum by width on the height of the ball"""
    new_height = (length ** 2 - width ** 2) ** 0.5
    return new_height

def update_acceleration():
    """Return the amount of acceleration using the gravity strength and
    the theta angle for x coordinate and the substraction the vertical from
    the new height and the same but with old height witch is coords.y - top_pen.y"""
    return gr.Point(G * theta, (height - vertical) - ((coords.y - top_pen.y) - vertical))

def create_cord(size):
    """Creates a cord using circles between the ball and the top of the pendulum.
    Global function creates unique names for each circle started by circle_0"""
    dist_x = width/(amount+1)                #  distance between the circles by x
    dist_y = height/(amount+1)               #  distance between the circles by y
    for k in range(amount):
        coords_circle = gr.Point(dist_x*(k+1) + top_pen.x, dist_y*(k+1) + top_pen.y)
        globals()['circle_%s' % k] = gr.Circle(coords_circle, size)
        globals()['circle_%s' % k].setFill('black')
        globals()['circle_%s' % k].draw(window)
        globals()['coords_circle_%s' % k] = coords_circle

def move_cord():
    """Moving the circles in the cord using just velocity of the ball.
    Global function calls the unique names for each circle to move"""
    dist_x = velocity.x/(amount+1)           #  distance inside the velocity between the circles by x
    dist_y = velocity.y/(amount+1)           #  distance inside the velocity between the circles by y
    for k in range(amount):
        velocity_circle = gr.Point(dist_x*(k+1), dist_y*(k+1))
        globals()['velocity_circle_%s' % k] = velocity_circle
        globals()['circle_%s' % k].move(globals()['velocity_circle_%s' % k].x,
                                        globals()['velocity_circle_%s' % k].y)

window = gr.GraphWin("Model", 800, 800)

G = 0.02                                     #  gravity strength
velocity = gr.Point(0, 0)                    #  velocity
acceleration = gr.Point(0, 0)                #  acceleration
top_pen = gr.Point(400, 180)                 #  top pendulum point
start_point = gr.Point(600, 500)             #  starting coordinates
vertical = start_point.y - top_pen.y         #  line between the top point of the pendulum and the middle point
                                             #  of the pendulum by width on the height of the start point
width = start_point.x - top_pen.x            #  width between the ball and the middle of the pendulum
length = (width ** 2 + vertical ** 2) ** 0.5 #  length of the pendulum
height = update_height()                     #  (details in description of the function)
coords = start_point                         #  first coordinates

top = gr.Circle(top_pen, 12)                 #  create a top of the pendulum
top.setFill('black')                         #  fill the top of the pendulum
top.draw(window)                             #  draw the top of the pendulum

ball = gr.Circle(start_point, 28)            #  create a ball
ball.setFill('black')                        #  fill the ball
ball.draw(window)                            #  draw the ball

amount = 17                                  #  amount of circles in the cord
create_cord(5)                               #  creates cord by circles where argument is a size of the circles

while True:
    coords = add(coords, velocity)           #  update coords
    width = coords.x - top_pen.x             #  update width
    height = update_height()                 #  (details in description of the function)
    theta = update_theta()                   #  it is angle (details in description of the function)
    acceleration = update_acceleration()     #  (details in description of the function)
    velocity = add(velocity, acceleration)   #  update velocity by adding the acceleration
    ball.move(velocity.x, velocity.y)        #  move the ball using velocity values
    move_cord()                              #  move the cord (details in description of the function)

    window.checkMouse()                      #  enable a closing of the window
    gr.time.sleep(0.001)                     #  delay between iterations
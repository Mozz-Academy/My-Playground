import turtle
import random
import time

w = turtle.Screen()
w.setup(width=500, height=500)
w.title('Snake Game')
w.tracer(100)

y = 230
posX = 46 * random.randint(-5, 4) + 23
posY = 46 * random.randint(-5, 4) + 23
segments = []
score = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.pensize(5)
pen.pencolor('blue')
pen.goto(-230, 230)
pen.pendown()

player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.shapesize(stretch_wid=2)
player.color('lime')
player.goto(-207, 207)

obj = turtle.Turtle()
obj.speed(0)
obj.penup()
obj.shape("square")
obj.shapesize(stretch_wid=2)
obj.color('red')
obj.goto(posX, posY)



for i in range(10):
    for row in range(10):
        pen.pendown()
        for cell in range(4):
            pen.forward(46)
            pen.right(90)
        pen.penup()
        pen.forward(46)
    y = y - 46
    pen.goto(-230, y)

def right():
    player.right(90)
def left():
    player.left(90)
def move():
    player.forward(46)
    time.sleep(0.4)

w.listen()
w.onkeypress(left, 'Left')
w.onkeypress(right, 'Right')


while True:
    posX = 46 * random.randint(-5, 4) + 23
    posY = 46 * random.randint(-5, 4) + 23
    w.update()

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = player.xcor()
        y = player.ycor()
        segments[0].goto(x, y)

    move()

    if player.distance(obj) < 23:
        new = turtle.Turtle()
        new.speed(0)
        new.penup()
        new.shape("square")
        new.shapesize(stretch_wid=2)
        new.color('lime')
        new.goto(player.xcor(), player.ycor())
        segments.append(new)

        obj.goto(posX, posY)
        score += 1
        w.title('Snake Game | ' + str(score))


    if player.xcor() > 230 or player.xcor() < -230 or player.ycor() < -230 or player.ycor() > 230:
        quit()

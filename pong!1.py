import turtle 

#window
window = turtle.Screen()
window.title("Pong!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#score
scoreA = 0
scoreB = 0

#paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350, 0)

#paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.13

#pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))

def paddle_a_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddle_a_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)
    
def paddle_b_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddle_b_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

#controls
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #paddle limits
    if paddleA.ycor() + 50 >= 300:
        paddleA.sety(250)

    if paddleA.ycor() - 50 <= -300:
        paddleA.sety(-250)

    if paddleB.ycor() + 50 >= 300:
        paddleB.sety(250)

    if paddleB.ycor() - 50 <= -300:
        paddleB.sety(-250)

    #ball movment
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
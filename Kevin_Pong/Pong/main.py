import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scoring
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# This speed since it's going hella fast on my computer
ball.dx = .09
ball.dy = .09

# Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0                         Player B: 0", align="center", font=("Ariel", 24, "normal"))

 # Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 60
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 60
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 60
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 60
    paddle_b.sety(y)

# Keybinds
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# main game loop
while True:
    wn.update() # continual updating of ball movement

    #Moving Ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #Stopping paddles from going to infinity and beyond
    if paddle_a.ycor() > 300:
        paddle_a.goto(-350, 300)
    if paddle_a.ycor() < -300:
        paddle_a.goto(-350, -300)

    if paddle_b.ycor() > 300:
        paddle_b.goto(350, 300)
    if paddle_b.ycor() < -300:
        paddle_b.goto(350, -300)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("tap.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("tap.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}                         Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))
        winsound.PlaySound("haha.wav", winsound.SND_ASYNC) #haha
        # Resetting paddles to starting position
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}                         Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))
        winsound.PlaySound("haha.wav", winsound.SND_ASYNC) #haha
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)

    #Paddle + Ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("psound.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("psound.wav", winsound.SND_ASYNC)

    if score_a >= 5:
        ball.goto(0, 0)
        ball.dx = .00
        ball.dy = .00
        pen.clear()
        pen.write("Player A has won since player B sucks too hard", align="center", font=("Ariel", 24, "normal"))

    if score_b >= 5:
        ball.goto(0, 0)
        ball.dx = .00
        ball.dy = .00
        pen.clear()
        pen.write("Player B has won since player A sucks too hard", align="center", font=("Ariel", 24, "normal"))
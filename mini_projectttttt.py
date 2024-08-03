import turtle

form = turtle.Screen()
form.title("Ping Pong Game By Mirna & Onay & Mariam (Team 10)")
form.setup(width=800, height=600)
form.tracer(0)  
form.bgcolor("green")


ball = turtle.Turtle()
ball.speed(8)  
ball.shape("circle")
ball.color("white")

ball.shapesize(stretch_len=1, stretch_wid=1)
ball.goto(0,0)  
ball.penup()  
ball_dx, ball_dy = 1, 1
ball_speed = .3


player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.color("blue")
player1.penup()
player1.goto(-350,0)


player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.color("red")
player2.penup()
player2.goto(350,0)


score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0,260)
score.write("Player1: 0 Player2: 0", align="center",
            font=("Courier", 14, "normal"))
score.hideturtle()  
p1_score, p2_score = 0,0  

players_speed = 30


def p1_move_up():
    player1.sety(player1.ycor() + players_speed)


def p1_move_down():
    player1.sety(player1.ycor() - players_speed)


def p2_move_up():
    player2.sety(player2.ycor() + players_speed)


def p2_move_down():
    player2.sety(player2.ycor() - players_speed)



form.listen()  
form.onkeypress(p1_move_up, "w")  
form.onkeypress(p1_move_down, "s")
form.onkeypress(p2_move_up, "Up")
form.onkeypress(p2_move_down, "Down")



while True:
    form.update()

    
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))

    
    if(ball.ycor() > 290):   
        ball.sety(290)
        ball_dy *= -1  

    if(ball.ycor() < -290):   
        ball.sety(-290)
        ball_dy *= -1  


    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

    
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() >(player2.ycor()-60)and ball.ycor() < (player2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1

    
    if(ball.xcor() > 390):
        ball.goto(0, 0)
        ball_dx *= -1  
        score.clear()
        p1_score += 1
        score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))

    if(ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1  
        score.clear()
        p2_score += 1
        score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))

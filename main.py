from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600,)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "p")
screen.onkey(r_paddle.down, ";")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 60 and ball.xcor() > 330 or ball.distance(l_paddle) < 60 and ball.xcor() < -330:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.change_direction()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.change_direction()
        scoreboard.r_point()


screen.exitonclick()
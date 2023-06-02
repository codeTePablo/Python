from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
# main 

# objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_stop = True
while game_stop:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        print("bounce")
        ball.bounce_x() 

    if ball.xcor() > 300:
        ball.restart() 

    if ball.xcor() < -300:
        ball.restart()

screen.exitonclick()
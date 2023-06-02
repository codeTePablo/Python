from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# object 
snake = Snake()
food = Food()
score = ScoreBoard()

# move
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    # detect collision with food
    # distance is 15 (margen) because the circle is 10 x 10 
    if snake.head.distance(food) <= 15:
        # collision print this
        # print("eat")
        food.refresh()
        # increment score 
        snake.extend_body()
        score.increment_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for body in snake.body[1:]:
        if snake.head.distance(body) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()
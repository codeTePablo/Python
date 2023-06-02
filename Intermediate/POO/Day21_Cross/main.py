from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time
# objects

car = CarManager()
player = Player()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_stop = True
while game_stop:
    screen.update()
    time.sleep(0.01)
    car.create_cars()
    car.move_cars()

    for i in car.cars:
        if i.distance(player) < 20:
            print("dead")
            game_stop = False

    if player.finish():
        player.restart_position()
        car.speed()


screen.exitonclick()
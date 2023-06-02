from turtle import Turtle
import random as rd
starting_move_distance = 3
move_increment = 10

class CarManager():

    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = starting_move_distance
    
    def create_cars(self):
        random_chance = rd.randint(1,13)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color("white")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = rd.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(starting_move_distance)

    def speed(self):
        self.car_speed += move_increment
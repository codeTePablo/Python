from turtle import Turtle 
import random as rd

# inherit of turtle to create food  
class Food(Turtle):
    
    def __init__(self):
        # super class
        super().__init__()
        self.shape("circle")
        self.penup()
        # 10 x 10 circle 
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = rd.randint(-200, 200)
        random_y = rd.randint(-200, 200)
        # 
        self.goto(random_x, random_y)

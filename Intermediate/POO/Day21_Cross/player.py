from turtle import Turtle

starting_position = (0, -280)
move_distance = 10
move_distance_down = -10

finish_line_y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.restart_position()

    def restart_position(self):
        self.goto(starting_position)


    def finish(self):
        if self.ycor() > finish_line_y:
            return True
        else:
            return False

    def go_up(self):
        self.forward(move_distance)

    def go_down(self):
        self.forward(move_distance_down)
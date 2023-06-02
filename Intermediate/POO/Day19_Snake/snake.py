from turtle import Turtle
start_position = [(0,0), (-20,0), (-40,0)]
move_distance = 10
up = 90
down = 270
left = 180
right = 0


class Snake:
    
    def __init__(self) -> None:
        self.body = []
        self.create_snake()
        # head of snake at the position 0 
        self.head = self.body[0]
    
    def create_snake(self):
        for i in start_position:
            self.add_body(i)

    def add_body(self, position):
        head = Turtle("square")
        head.color("white")
        head.penup()
        head.goto(position)
        self.body.append(head)

    def reset(self):
        for seg in self.body:
            # disappear of the screen 
            seg.goto(700,700)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]


    def extend_body(self):
        self.add_body(self.body[-1].position())

    def move(self):
            # len(body) = 3 -1 = 2, stop = 0, steps = -1
        for seg_num in range(len(self.body) - 1, 0, -1):
            # new_x = for i in body[0 - 1], body[1-1] 
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            # body[i] go to (inside for i)
            self.body[seg_num].goto(new_x, new_y)
        # move the head 
        self.body[0].forward(move_distance)

    def up(self):
        # up
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        # down, 
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        # left, 
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):    
        # right
        if self.head.heading() != left:
            self.head.setheading(right)
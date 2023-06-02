import turtle as t
import random as rd

me = t.Turtle()

# line
# for _ in range(10):
#     me.forward(10)
#     me.penup()
#     me.forward(10)
#     me.penup()

# color = ["red", "blue"]
# # triangle = 180
# def draw_shape(side):
#     # side = 3
#     # 3 moves
#     for _ in range(side):
#         angle = 360 / side # 60
#         me.forward(100) # move
#         me.right(angle) # move with angle

# for shape_side in range(3,11):
#     # increment one line in the shape like the function in range
#     # triangle, square, pentagon, hexagon, etc.
#     me.color(rn.choice(color))
#     draw_shape(shape_side)

# using tuple
t.colormode(255)


def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    color = (r, g, b)
    return color


# # random walk
# # steps = 10
# directions = [0,90,180,270]

# for _ in range(200):
#     me.color(random_color())
#     me.forward(30)
#     me.setheading(rd.choice(directions))


for _ in range(1, 36):
    me.circle(100)
    # initial position
    current_heading = me.heading()
    # increment position in 10 u
    me.setheading(current_heading + 10)

my_screen = t.Screen()
my_screen.exitonclick()

import turtle
import pandas as pd 

screen = turtle.Screen()
image = "blank_states_img.gif"
# crate my shape
turtle.shape("circle")
# import image to show in screen 
screen.addshape(image)
turtle.shape(image)

def check_coordenates(state,x,y):
    """ return coordenates in the map on screen """
    # print in image the state 
    print(x,y)

# import data 
data_states = pd.read_csv("50_states.csv")
all_states = data_states.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    asnwer_state = screen.textinput(title=f"{len(guessed_states)}", 
                                    prompt="What's a another state's name").title()
    print(asnwer_state)
    if asnwer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_date = pd.DataFrame(missing_states)
        new_date.to_csv("Missing states")
        break
    if asnwer_state in all_states:
        guessed_states.append(asnwer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data_states[data_states.state == asnwer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(asnwer_state)

import turtle
import pandas
from display_states import Display


screen = turtle.Screen()
screen.title("india-state-game")
img = "india_map.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("29_states_data.csv")
state_list = data.state.tolist()
x_cord = data.x.tolist()
y_cord = data.y.tolist()


state_count = 0

while True:

    if state_count == 28:
        break

    answer_state = screen.textinput(title=f"{state_count}/29 states correct",
                                    prompt="what is the state name").title()

    if answer_state == "Exit":

        dt = {
            "state": state_list,
            "x": x_cord,
            "y": y_cord
        }

        dta = pandas.DataFrame(dt)
        dta.to_csv("missed_states.csv")
        break

    if answer_state in state_list:

        state_count += 1
        c = state_list.index(answer_state)
        disp = Display(x_cord[c], y_cord[c], answer_state)
        del state_list[c]
        del x_cord[c]
        del y_cord[c]

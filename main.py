import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(800, 800)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []

num_states = 0
while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{num_states}/50 States Correct",
                                     prompt="What's another state name?")).title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        num_states += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer_state]
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)

# s = set(guessed_states)
# missed_states = [x for x in states_list if x not in s]
# data_dict = {
#     "states": [missed_states]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("states_to_learn.csv")

turtle.mainloop()

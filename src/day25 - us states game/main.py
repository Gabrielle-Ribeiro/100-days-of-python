import pandas as pd
import turtle

from pandas._libs import missing

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv('50_states.csv')
num_states = 0
guessed_states = []

while num_states < 50:
    user_answer = str.title(screen.textinput(title=f'{num_states}/50 - Guess the State', 
                            prompt="What's another state's name?"))

    if user_answer == "Exit":
        missing_states = [state_name for state_name in states['state'] if state_name not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    for state_name in states['state']:
        if not user_answer in guessed_states and state_name == user_answer:
            s = turtle.Turtle()
            s.hideturtle()
            s.penup()
            s_data = states[states.state == state_name]
            s.goto(int(s_data.x), int(s_data.y))
            s.write(state_name)
            num_states += 1
            guessed_states.append(state_name)
            break

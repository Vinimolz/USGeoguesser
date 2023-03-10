import csv
import pandas
import turtle

def main():
    screen = turtle.Screen()
    screen.title = 'U.S GeoGuesser'
    background_image_path = 'blank_states_img.gif'
    screen.addshape(background_image_path)
    turtle.shape(background_image_path) 
    
    data = pandas.read_csv("data/50_states.csv") 

    guessed_states = []

    state_data_list = get_states_data_list()    
    
    while len(guessed_states) < 50:
        user_input = screen.textinput(f'U.S Geoguesser {len(guessed_states)}/50',
                                       'Guess the name of a state').title()
        
        if user_input == 'Exit':
            missing_states = []
            for state in state_data_list:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break

        if user_input in state_data_list:
            guessed_states.append(user_input)

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == user_input]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(user_input)
    

def get_all_data():
    weather_data = []
    with open("data/weather_data.csv") as weather_data_file:
        data = csv.reader(weather_data_file)
        for row in data:
            weather_data.append(row)
    return weather_data

def get_int_temp():
    temperature_list = []
    with open("data/weather_data.csv") as weather_data_file:
        data = csv.reader(weather_data_file)
        for row in data:
            if row[1] != "temp":
                temperature_list.append(int(row[1]))
                
    return temperature_list

def get_data_with_pandas():
    data = pandas.read_csv('data/weather_data.csv')
    print(data)

def get_squirrel_data():
    data = pandas.read_csv("data/squirrel_data.csv")
    return data

def get_states_data_list():
    data = pandas.read_csv('data/50_states.csv')
    data = data.state.to_list()
    return data

if __name__ == '__main__':
    main()
import csv
import pandas

def main():
   squirrel_data = get_squirrel_data()
   print(squirrel_data)

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

if __name__ == '__main__':
    main()
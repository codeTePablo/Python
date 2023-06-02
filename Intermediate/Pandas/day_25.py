# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

import csv
import pandas as pd

# with out using pandas, so much code!

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     # list to contain all temperatures 
#     temperatures = []
#     # object 
#     print(data)
#     # object to do for loop to show all data in a list 
#     # for row in data:
#     #     print(row)

#     # show only temp data 
#     for temp in data:
#         temperatures.append(temp[1])
#     print(temperatures)

data = pd.read_csv("weather_data.csv")
# each column is a series in pandas
# print data temperature 
print(data["temp"])

# convert all data into a dictionary 
data_dict = data.to_dict()
print(data_dict) # 'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday'

temp_list = data["temp"].to_list()
# return the list of temperature 
print(temp_list)

def average(temp_list):
    """ return the average of the list of temperatures """
    return sum(temp_list) / len(temp_list)

print(average(temp_list))

# now with pandas is like...
# mean = average in this column 
print(data["temp"].mean())

# print the max value
print(data["temp"].max())

# get data in columns 
print(data["condition"])
# or 
# print(data.condition)

# get data of a row 
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# create dataframe from scratch 
data_dict = {
    "students": ["Amy", "James", "Angela"], 
    "scores": [1,2,3]
}

data_students = pd.DataFrame(data_dict) 
print(data_students)
# adding data into a new file .csv
data.to_csv("new_data.csv")

data_central = pd.read_csv("Central_Park.csv")
gray = len(data_central[data_central["Primary Fur Color"] == "Gray"])
cinnammon = len(data_central[data_central["Primary Fur Color"] == "Cinnammon"])
black = len(data_central[data_central["Primary Fur Color"] == "Black"])
print((data_central[data_central["Primary Fur Color"] == "Gray"]))

data_dict_central = {
    "Color": ["Gray", "Cinnammon", "Black"],
    "Count": [gray, cinnammon, black]
}
data_central_frame = pd.DataFrame(data_dict_central)
print(data_central_frame) 

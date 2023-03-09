import pandas

# with open('weather_data.csv') as data:
#     weather_data = [x.strip() for x in data.readlines()]
#
# print(weather_data)

# import csv
#
# with open('weather_data.csv') as data:
#     data = csv.reader(data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv('weather_data.csv')

# print(data['temp'])
# print(type(data))

"""
pandas 2 core data types: series and dataframe
series are a column, dataframe are a whole table. 
series = 1 dimensional, dataframe = 2 dimensional
"""

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)

# print((data['temp'].mean()))
# print(data['temp'].max())

# print(data['condition'])
# print(data.condition)

# get data in row, filter a column by a condition
# print(data[data.day == "Monday"])
# monday = data[data.day == "Monday"]
# monday_fahrenheit = (monday.temp * 1.8) + 32
# print(monday_fahrenheit)

# print(data[data.temp == data.temp.max()])

# create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# new_data = pandas.DataFrame(data_dict)
# print(new_data)

# with open('./students_score.txt', mode="w") as new_text:
#     new_text.write(new_data.to_csv())
# new_data.to_csv('students_score_2.csv')

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(squirrel_data.columns)

squirrel_count = {}
primary_squirrel_colors = squirrel_data["Primary Fur Color"].unique().tolist()

for color in primary_squirrel_colors:
    if isinstance(color, str):
        squirrel_count[color] = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])

data_dict = {
    "Fur Color": [],
    "Count": []
}
for x in squirrel_count:
    data_dict["Fur Color"].append(x)
    data_dict["Count"].append(squirrel_count[x])

data_dict = pandas.DataFrame(data_dict)
# data_dict.to_csv('squirrel_count.csv')


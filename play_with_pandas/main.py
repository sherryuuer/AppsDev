# import csv

# with open("play_with_pandas/weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temperatures.append(int(temp))
#     print(temperatures)

# # instead, use pandas.
# import pandas


# data = pandas.read_csv("play_with_pandas/weather_data.csv")
# temp_list = data["temp"].to_list()
# print(sum(temp_list) / len(temp_list))

# mean_temp = data["temp"].mean()
# print(mean_temp)

# max_temp = data["temp"].max()  # data.temp
# print(max_temp)

# # get data in row.
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()].condition)

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp)
# print(monday_temp_F)

# data_dict = {
#     "student": ["Ana", "James", "Joy"],
#     "score": [90, 78, 80]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("play_with_pandas/score_data.csv")

import pandas as pd


data = pd.read_csv("play_with_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fury_count = data.groupby("Primary Fur Color").count()
fury_count = fury_count.X.rename("count")
fury_count.to_csv("play_with_pandas/squirrel_count.csv")

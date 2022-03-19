import pandas
# # import csv

# # f = open("../../Desktop/100 Days of python/Day-25/weather-data.csv", "r")
# # data = f.readlines()
# # print(data)

# # with open("../../Desktop/100 Days of python/Day-25/weather-data.csv") as file:
# #     data = csv.reader(file)
# #     tempeatures = []
# #     for row in data:
# #         if row[1] != "temp":

# #             temputure = int(row[1])
# #             tempeatures.append(temputure)


# # print(tempeatures)

# data = pandas.read_csv(
#     "../../Desktop/100 Days of python/Day-25/weather-data.csv")
# data_dic = data.to_dict()
# # print(data_dic)

# data_list = data["temp"].to_list()
# # avg = sum(data_list)/len(data_list)
# # print(f"The average is {round(avg,2)}")
# avg = data["temp"].mean()
# # print(avg)

# max_temp = data["temp"].max()
# # print("max temperature is", max_temp)

# # * Get data in column
# # print(data["condition"])
# # print(data.condition)

# # * Get dat in row
# # print(data[data.day == "Monday"])

# # Get whole data row for max temperature
# # print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print((monday.temp*1.8)+32)

# # *  Create new dataframe

# data_dic = {
#     "students": ["Jesse", "monica", "sara"], "score": [78, 66, 92]
# }


# new_data = pandas.DataFrame(data_dic)
# new_data.to_csv("new_data.csv")

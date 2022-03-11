import pandas
# import csv

# f = open("../../Desktop/100 Days of python/Day-25/weather-data.csv", "r")
# data = f.readlines()
# print(data)

# with open("../../Desktop/100 Days of python/Day-25/weather-data.csv") as file:
#     data = csv.reader(file)
#     tempeatures = []
#     for row in data:
#         if row[1] != "temp":

#             temputure = int(row[1])
#             tempeatures.append(temputure)


# print(tempeatures)

data = pandas.read_csv(
    "../../Desktop/100 Days of python/Day-25/weather-data.csv")
print(data["temp"])

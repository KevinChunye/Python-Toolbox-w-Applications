"""
# with open() as approach to open csv
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

# import csv approach in reading csv file
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
            print(row)
    print(temperatures)
"""
import pandas as pd

df = pd.read_csv("weather_data.csv")
#print(type(df))

"""
data_dict = df['temp'].to_dict()
print(data_dict)

temp_list = df['temp'].to_list()
print(temp_list)

# print the avg temp
print(sum(temp_list)/len(temp_list))

print(df['temp'].mean())
print(df['temp'].max())

#print(df['condition'])
# pandas converts all the column into attributes of the df
# better to name all columns in lower case
print(df.condition)
"""
# get data in row
print(df[df.day == "Monday"])
# find the max temp row
print(df[df.temp == df.temp.max()])

monday = df[df.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 +32
print(monday_temp_F)

f_list= []
for temp in df['temp']:
    f_temp = temp *9/5 +32
    f_list.append(f_temp)

print(f_list)

# create a df from scratch
data_dict = {
    "students" :["A","B","C"],
    "scores" : [76,56,65]
}
data = pd.DataFrame(data_dict)
print(data)